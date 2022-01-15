import urllib3
import logging
import os
import time

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

TARGET_FOLDER = r'D:\data\edgar\sampling\submissions'
CANDIDATE_FILES_SRC = r'd:\workspace\edgar-abs-kg\dataset\mbs-index.txt'
DOWNLOADED_FILES_SRC = r'd:\workspace\edgar-abs-kg\dataset\mbs-index-downloaded.txt'

candidate_files = set()
downloaded_files = set()
pending_download = set()

http = urllib3.PoolManager(timeout= 90)
SEC_HOST = 'https://sec.gov'
def parse_lines_in_file(filename):
    logging.info("parsing file: {}".format(filename))
    file = open(filename, 'r')
    lines = list()
    try:
        lines_origin = file.readlines()
        for line in lines_origin:
            lines.append(line[:-1])
    finally:
        file.close()
    logging.info("Total num of lines in file: {} - [{}]".format(filename, len(lines)))
    return lines

def init_candidate_files():
    candidate_file_list = parse_lines_in_file(CANDIDATE_FILES_SRC)
    candidate_files.update(candidate_file_list)
    logging.info("Candidate files - {}".format(len(candidate_files)))

def init_downloaded_files():
    downloaded_file_list = parse_lines_in_file(DOWNLOADED_FILES_SRC)
    downloaded_files.update(downloaded_file_list)
    logging.info("Downloaded files - {}".format(len(downloaded_files)))

def calc_pending_download_file():
    pending_download.update(candidate_files.difference(downloaded_files))
    logging.info("Totoal num of pending download files: {}".format(len(pending_download)))

def do_download_file(filename):
    url = filename
    logging.info("Downloading: {}".format(url))

    headers = {
        'User-Agent':'edgar@yahoo.com',
        'Accept-Encoding': 'gzip, deflate',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
    }
    response = http.request('GET',url, headers=headers)
    
    with open(os.path.join(TARGET_FOLDER, filename.split('/')[-1]),'w') as file:
        file.write(response.data.decode('utf-8'))
def record_downloaded_file(filename):
    with open(DOWNLOADED_FILES_SRC,'a') as downloaded_file:
        downloaded_file.write(filename+'\n')
def download_file(filename, pending_cnt, current_idx):
    logging.info('[{}/{}]Start download file: {}'.format(current_idx, pending_cnt, filename))
    # try:
    do_download_file(filename)
    record_downloaded_file(filename)
    # except err:
    #     pass

def download_files():
    pending_cnt = len(pending_download)
    current_idx = 0
    for pending_file in pending_download:
        try:
            download_file(pending_file,pending_cnt, current_idx)
            time.sleep(0.1)
        except Exception as err:
            logging.error("Faile to download: {}".format(pending_file),str(err))
        current_idx = current_idx + 1 

if __name__ == '__main__':
    init_candidate_files()
    init_downloaded_files()
    calc_pending_download_file()
    download_files()