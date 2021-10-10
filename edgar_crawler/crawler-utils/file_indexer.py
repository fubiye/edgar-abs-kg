import zipfile
import pandas as pd
import os

# FILE = r'D:\data\edgar\Archives_20210607_01_44.zip'

FILE_INDEX = r'D:\data\edgar\file_index.csv'

def parse_zip_file(zip_file):
    zip_file_name = os.path.basename(zip_file)
    print("Parsing: {}".format(zip_file_name))
    ZIP_FILE = zipfile.ZipFile(zip_file)
    zipDf = pd.DataFrame()
    zipDf['file_name'] = pd.Series(ZIP_FILE.namelist())
    zipDf['file_name'] = zipDf['file_name'].apply(lambda name: None if name[-1:] == '/' else name)
    zipDf.dropna(inplace=True)
    zipDf['zip_file_name'] = zip_file_name
    return zipDf

def index_file(zip_file):
    df = pd.read_csv(FILE_INDEX)
    indexed_zips = df['zip_file_name'].unique()
    zipDf = parse_zip_file(zip_file)
    df = df.append(zipDf, ignore_index=True)
    df.to_csv(FILE_INDEX, index=False)

if __name__ == '__main__':
    S3_PATH = r'E:\dataset\edgar\enrich\s3'
    cnt = 0
    df = pd.read_csv(FILE_INDEX)
    indexed_zips = df['zip_file_name'].unique()

    for s3_file in os.listdir(S3_PATH):
        cnt += 1
        print("#{} - {}".format(cnt, s3_file))
                
        if s3_file[-3:] != 'zip':
            continue
        if s3_file in indexed_zips:
            print("Zip file has been indexed: {}".format(s3_file))
            continue
        index_file(os.path.join(S3_PATH,s3_file))
        
        
