import os
import json
BASE_DIR = r'D:\data\edgar\sampling\Archives\edgar\data'

if __name__ == '__main__':
    index = dict()
    for cik in os.listdir(BASE_DIR):
        for accession in os.listdir(os.path.join(BASE_DIR, cik)):
            for fileName in os.listdir(os.path.join(BASE_DIR, cik, accession)):
                index[accession] = {
                    "cik": cik,
                    "accession": accession,
                    "fileName": fileName
                }
    with open('index_by_accession.json', 'w') as index_json:
        json.dump(index, index_json)
