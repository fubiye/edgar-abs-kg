import pandas as pd
import zipfile
import os
import shutil
import time

FILE_INDEX_FILE = r'D:\data\edgar\file_index.csv'
VALID_INDEX_FILE_INDEX = r'D:\data\edgar\valid_file_index.csv'
S3_ZIP_FILE = r'D:\data\edgar'
MERGE_PATH = r'D:\dataset\edgar\merge'
# df = df[df['file_name'].str.contains('/1000112/')]
# print(df)
valid_patterns = set()

def parse_lines_in_file(filename):
    file = open(filename, 'r')
    lines = list()
    try:
        lines_origin = file.readlines()
        for line in lines_origin:
            lines.append(line[:-1])
    finally:
        file.close()
    return lines
def is_valid_file(filename):
    for pattern in valid_patterns:
        if pattern in filename:
            return True
    return None
def filter_valid_files():
    ciks = set(parse_lines_in_file('cik.txt'))
    for cik in ciks:
        valid_patterns.add('/{}/'.format(cik))
    finalDf = finalDf = pd.DataFrame()
    df = pd.read_csv(FILE_INDEX_FILE)
    df['valid'] = df['file_name'].apply(is_valid_file)
    df.dropna(inplace=True)
    df.to_csv(VALID_INDEX_FILE_INDEX, index=False)
    print(df)
def extract_file(archive, filename):
    archive.extract(filename, MERGE_PATH)
def extract_files(zipGrp):
    zipFileName = zipGrp[0]
    print("Extracting {}....".format(zipFileName))
    archive = zipfile.ZipFile(os.path.join(S3_ZIP_FILE, zipFileName))
    filesDf = zipGrp[1]
    filesDf['file_name'].apply(lambda filename: extract_file(archive, filename))
if __name__ == '__main__':
    parsed_records = set(parse_lines_in_file('record.txt'))
    parsed_records = parsed_records.union(set(parse_lines_in_file('failed.txt')))
    
    df = pd.read_csv(VALID_INDEX_FILE_INDEX)
    byZip = df.groupby("zip_file_name")
    zip_file_len = len(byZip)

    with open('record.txt','a') as records:
        index = 0
        for zipGrp in byZip:
            zipFileName = zipGrp[0]
            if zipFileName != 'Archives_20210607_01_44.zip':
                continue
            index += 1
            print("[{}/{}] -  {}".format(index, zip_file_len, zipFileName))
            if zipFileName in parsed_records:
                print("Skipping file: {}".format(zipFileName))
                continue
            try:
                extract_files(zipGrp)
                records.write(zipGrp[0])
                records.write('\n')
                records.flush()
                # if index % 100 == 0:
                #     zipFilePath = os.path.join(r'D:\dataset\edgar', 'edgar' + str(int(time.time())*1000))
                    # shutil.make_archive(zipFilePath, 'zip', MERGE_PATH)
                    # shutil.rmtree(MERGE_PATH)
            except:
                with open('failed.txt','a') as failed:
                    failed.write(zipFileName)
                    failed.write('\n')
                    failed.flush()
                print("Failed to process files: {}".format(zipFileName))
                pass