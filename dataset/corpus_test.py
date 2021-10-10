import pandas as pd

df = pd.read_csv(r'D:\data\edgar\example\corpus.csv')
# df['FilingType'] = df['Content'].apply(lambda content: content[:content.index('\n')])
# df['ContentLen'] = df['Content'].apply(lambda content: len(content))
# print(df[df['FilingType'] == '10-D'])
# print(df[df['FilingType'] == '10-D']['Content'].iloc[0])
a = df[df['FilingType'] == '10-D']['Content'].iloc[0]
b = df[df['FilingType'] == '10-D']['Content'].iloc[1]
# from pprint import pprint
# from difflib import Differ
# d = Differ()
# result = list(d.compare(a, b))
# pprint(result)
print(a)
print("$****$")
print(b)