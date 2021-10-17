import pandas as pd 
import numpy as np
from nltk.tokenize import sent_tokenize
# import re

CORPUS = r'D:\data\edgar\example\corpus.csv'
# nlp = spacy.load("en_core_web_sm")
ends = '(\.|\!|\?)\s'
def cut_sentences(content):
    # text_sentences = nlp(content)
    # return text_sentences.sents
    sents = ' '.join(content.split('\n'))
    return [sent for sent in sent_tokenize(sents)]
    

if __name__ == '__main__':
    df = pd.read_csv(CORPUS)
    df['sents'] = df['Content'].apply(cut_sentences)
    sents = np.concatenate(np.array(df['sents']))
    sents = np.sort(sents)
    sents = np.unique(sents)
    print(len(sents))
    with open('sents.txt','w',encoding='utf-8') as sentsf:
          sentsf.writelines([sent+'\n' for sent in sents])