import sentencepiece as spm
# spm.SentencePieceTrainer.train(input='sents.txt', model_prefix='abs-sent-piece', vocab_size=10000)

sp = spm.SentencePieceProcessor(model_file = 'abs-sent-piece.model')
print(sp.encode('Master Servicers'))
print(sp.encode('Special Servicers'))

print(sp.decode([44, 1105]))
print(sp.decode([35, 1105]))

