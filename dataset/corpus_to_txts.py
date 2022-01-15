# coding=utf-8

import pandas as pd
from pathlib import Path
# extract corpus to seprate files
OUT_PUT_DIR = r'D:\data\edgar\example\documents'
df = pd.read_csv(r'D:\data\edgar\example\corpus.csv')
# def write_to_file(cik,filingId,fileName,content):
def write_to_file(cik,filingId,fileName,content):
    base_dir = Path(OUT_PUT_DIR)
    file_name = str(cik) + '+' + str(filingId) + '+' + str(fileName)
    file_name = file_name.replace('.htm', '.txt')
    (base_dir/file_name).write_text(content,encoding='utf-8')

df.apply(lambda row: write_to_file(row['CIK'],row['FilingId'],row['FileName'],row['Content']), axis=1)
