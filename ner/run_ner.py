import pandas as pd
import spacy
import os
from spacy import displacy
CORPUS = r'D:\data\edgar\example\corpus.csv'
nlp = spacy.load("en_core_web_sm")

def ner(file_name, content):
    #  = row["FileName"]
    # content = row["Content"]
    doc = nlp(content)
    html = displacy.render(doc, style="ent", page=True)
    with open(os.path.join(r'D:\data\edgar\example',file_name), "w", encoding='utf-8') as fo:
        fo.write(html)

if __name__ == '__main__':
  df = pd.read_csv(CORPUS)
#   randDf = df.sample(n = 5)
  randDf = df[df['FileName']=='msc17bk5_10k-2018.htm']
  print(randDf)
  randDf.apply(lambda row: ner(row['FileName'],row['Content']), axis=1)

