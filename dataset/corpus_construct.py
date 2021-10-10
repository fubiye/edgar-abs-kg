import pandas as pd
import os
import logging
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

DATA_PATH = r'D:\data\edgar\example'

def process_filings_of_cik(cik):
    filings = []
    # count = 0
    for filing_id in os.listdir(os.path.join(DATA_PATH, cik)):
        logging.info("CIK: {}, Filing ID: {}".format(cik, filing_id))
        files = process_filing(cik, filing_id)
        filings.extend(files)
        # count = count+1
        # if count >2:
        #     break
    return filings
def process_filing(cik, filing_id):
    files = []
    for filing_file in os.listdir(os.path.join(DATA_PATH, cik, filing_id)):
        if '.htm' not in filing_file:
            continue
        if '-index.htm' in filing_file:
            continue
        files.append(filing_file)
    logging.info("Filing ID: {}, Files: {}".format(filing_id, files))
    filings = []
    for filing_file in files:
        filings.append(parse_file(cik, filing_id,filing_file))
    return filings
def parse_file(cik, filing_id, file_name):
    soup = BeautifulSoup(open(os.path.join(DATA_PATH, cik, filing_id, file_name)),features='lxml')
    lines = ''.join(soup.findAll(text=True))
    lines = '\n'.join([line for line in lines.split('\n') if '' != line.strip()])
    return (cik, filing_id, file_name, lines)
if __name__ == '__main__':
    filings = []
    for cik in os.listdir(DATA_PATH):
        if not os.path.isdir(os.path.join(DATA_PATH, cik)):
            continue
        logging.info("processing filing files of cik {}".format(cik))
        filings.extend(process_filings_of_cik(cik))
    # print(parse_file('1706403', '000105640420003077', 'dbj17c06_10d-202003.htm'))
    logging.info("Generating dataframe...")
    df = pd.DataFrame(filings,columns=['CIK','FilingId','FileName','Content'])
    df.to_csv(os.path.join(DATA_PATH, 'corpus.csv'), index=None)
    logging.info("Saved corpus")