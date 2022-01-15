import os
import pandas as pd

BASE_DIR = r'D:\data\edgar\sampling\Archives\edgar\data'
ABS_DATA = r'D:\data\edgar\edgar_abs_universal.csv'

def get_ciks():
    ciks = set()
    for cik in os.listdir(BASE_DIR):
        # full_cik = cik.rjust(10,'0')
        # ciks.add(full_cik)
        ciks.add(int(cik))
    return ciks

if __name__ == '__main__':
    print("Start checking files")
    ciks = get_ciks()
    df = pd.read_csv(ABS_DATA)
    df['is_cmbs'] = df['cik'].apply(lambda cik: True if cik in ciks else False)
    df = df[df['is_cmbs'] == True]
    df['is_html'] = df['doc_link'].apply(lambda link: True if link[-3:] == 'htm' else False)
    df = df[df['is_html'] == True]
    docs = list(df['doc_link'])
    with open('mbs_docs.txt','w') as f:
        for doc in docs:
            f.write(doc)
            f.write('\n')