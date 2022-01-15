from pathlib import Path
import re
import numpy as np
import json
import torch
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForTokenClassification
from transformers import Trainer, TrainingArguments

def read_dataset(file_path):
    file_path = Path(file_path)

    raw_text = file_path.read_text(encoding='utf-8').strip()
    raw_docs = re.split(r'\n\t?\n', raw_text)
    token_docs = []
    tag_docs = []
    for doc in raw_docs:
        tokens = []
        tags = []
        for line in doc.split('\n'):
            token, tag = line.split('\t')
            tokens.append(token)
            tags.append(tag)
        token_docs.append(tokens)
        tag_docs.append(tags)

    return token_docs, tag_docs

def encode_tags(tags, encodings):
    labels = [[tag2id[tag] for tag in doc] for doc in tags]
    encoded_labels = []
    for doc_labels, doc_offset in zip(labels, encodings.offset_mapping):
        # create an empty array of -100
        doc_enc_labels = np.ones(len(doc_offset),dtype=int) * -100
        arr_offset = np.array(doc_offset)

        # set labels whose first offset position is 0 and the second is not 0
        doc_enc_labels[(arr_offset[:,0] == 0) & (arr_offset[:,1] != 0)] = doc_labels
        encoded_labels.append(doc_enc_labels.tolist())

    return encoded_labels

class ABSDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

if __name__ == '__main__':
    texts, tags = read_dataset('ner/abs.conll')
    unique_tags = set(tag for doc in tags for tag in doc)
    tag2id = {tag: id for id, tag in enumerate(unique_tags)}
    id2tag = {id: tag for tag, id in tag2id.items()}
    
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-cased')
    val_encodings = tokenizer(texts, is_split_into_words=True, return_offsets_mapping=True, padding=True, truncation=True)
    val_labels = encode_tags(tags, val_encodings)
    val_encodings.pop("offset_mapping")
    val_dataset = ABSDataset(val_encodings, val_labels)
    model = DistilBertForTokenClassification.from_pretrained('ner/abs-result', num_labels=len(unique_tags))
    training_args = TrainingArguments(
        output_dir='./abs-results',          # output directory
        num_train_epochs=5,              # total number of training epochs
        per_device_train_batch_size=32,  # batch size per device during training
        per_device_eval_batch_size=64,   # batch size for evaluation
        warmup_steps=500,                # number of warmup steps for learning rate scheduler
        weight_decay=0.01,               # strength of weight decay
        logging_dir='./logs',            # directory for storing logs
        logging_steps=10,
    )
    trainer = Trainer(
        model=model,                         # the instantiated 🤗 Transformers model to be trained
        args=training_args,                  # training arguments, defined above
        train_dataset=val_dataset,         # training dataset
        eval_dataset=val_dataset             # evaluation dataset
    )
    trainer.train()
    
    result = trainer.evaluate()
    with open('distilbert-base-cased-abs.json','w') as fp:
        json.dump(result, fp)
