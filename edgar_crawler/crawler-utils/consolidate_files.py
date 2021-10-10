import logging
import os
import zipfile

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

TARGET_FOLDER = 'd:\dataset\edgar\merge'
S3_FOLDER = r'D:\data\edgar\enrich\s3'

def uncompress_file(file):
    zFile = zipfile.ZipFile(file,'r')
    zFile.extractall(path=TARGET_FOLDER)
    zFile.close()

uncompress_file(r'D:\data\edgar\enrich\s3\Archieve202108221127.zip')
