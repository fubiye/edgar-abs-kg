import pandas as pd
import os
import logging
from bs4 import BeautifulSoup
import multiprocessing as mp

# Parsing HTML files under $DATA_PATH to csv file

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

DATA_PATH = r'D:\data\edgar\example'

NOT_STARTING_TAGS = set(['(','”)'])

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
    return [(cik, filing_id, f) for f in files]
def parse_file(filing_file):
    logging.info("Filing: {}".format(filing_file))
    cik, filing_id, file_name = filing_file
    content = open(os.path.join(DATA_PATH, cik, filing_id, file_name))
    html = ' '.join([line[:-1] for line in content.readlines()])
    soup = BeautifulSoup(html,features='lxml')
    tables = soup.findAll("table")
    if tables is not None:
        for table in tables:
            table.decompose()
    tokens = soup.findAll(text=True)
    tokens = [token.replace('\xa0','') for token in tokens]
    tokens = [token.strip() for token in tokens]
    tokens = [token for token in tokens if '' != token]
    lines = ''.join([' ' + token if (len(token) > 0 and token[0] in NOT_STARTING_TAGS) else ('\n' + token ) for token in tokens])
    return (cik, filing_id, file_name, lines[:lines.index('\n')].strip(), len(lines), lines)
if __name__ == '__main__':
    filings = []
    pool = mp.Pool(processes=16)
    for cik in os.listdir(DATA_PATH):
        if not os.path.isdir(os.path.join(DATA_PATH, cik)):
            continue
        logging.info("processing filing files of cik {}".format(cik))
        filing_files = process_filings_of_cik(cik)
        for filing_file in filing_files:
            filings.append(pool.apply_async(parse_file,[filing_file]))
    pool.close()
    pool.join()
    # print(parse_file('1706303', '000105640417003545', 'msc17bk5_10d-201707.htm'))
    logging.info("Generating dataframe...")
    df = pd.DataFrame([filing.get() for filing in filings],columns=['CIK','FilingId','FileName','FilingType','ContentLen','Content'])
    df.to_csv(os.path.join(DATA_PATH, 'corpus.csv'), index=None)
    logging.info("Saved corpus")