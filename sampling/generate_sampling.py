import pandas as pd
import numpy as np
import zipfile

UNAVALIABLE_FILES = 'unavailable.txt'
EDGAR_ZIP_FILE = r'D:\data\edgar\Archives_20210607_01_44.zip'
EDGAR_ZIP = zipfile.ZipFile(EDGAR_ZIP_FILE)

filing_files_df = pd.read_csv(r'sampling_filing_files_2000.csv')
doc_links = filing_files_df['doc_link']
doc_links = np.array(doc_links).tolist()

unavaliable_files = list()
for link in doc_links:
    print(link)
    try:
        EDGAR_ZIP.extract(link[1:], r'D:\data\edgar\sampling')
    except Exception as err:
        unavaliable_files.append(link)

with open(UNAVALIABLE_FILES,'a') as u_file:
    for filename in unavaliable_files:
        u_file.write(filename+'\n')