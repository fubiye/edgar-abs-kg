import urllib3
import logging
import os
import time

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
TARGET_FOLDER = r'/home/fubiye/storage/data/edgar/test'
CANDIDATE_FILES_SRC = 'files.txt'
DOWNLOADED_FILES_SRC = 'downloaded.txt'
SEC_HOST = 'https://sec.gov'

candidate_files = set()
downloaded_files = set()
pending_download = set()

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

def ensure_exists(filename):
    file_path = os.path.join(TARGET_FOLDER,filename[1:])
    parent_folder = os.path.dirname(file_path)
    logging.info("ensure folder exists: {}".format(parent_folder))
    if not os.path.exists(parent_folder):
        logging.info('parent folder not exists: {}'.format(parent_folder))
        os.makedirs(parent_folder)
        logging.info('folder created: {}'.format(parent_folder))

def do_download_file(filename):
    url = SEC_HOST + filename
    logging.info("Downloading: {}".format(url))

    headers = {
        'User-Agent':'edgar@yahoo.com',
        'Accept-Encoding': 'gzip, deflate',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'Host': 'www.sec.gov'
    }
    http = urllib3.PoolManager()
    response = http.request('GET',url, headers=headers)
    with open(os.path.join(TARGET_FOLDER, filename[1:]),'w') as file:
        file.write(response.data.decode('utf-8'))
def record_downloaded_file(filename):
    with open(DOWNLOADED_FILES_SRC,'a') as downloaded_file:
        downloaded_file.write(filename+'\n')
def download_file(filename):
    logging.info('Start download file: {}'.format(filename))
    ensure_exists(filename)
    do_download_file(filename)
    record_downloaded_file(filename)

def download_files():
    for pending_file in pending_download:
        try:
            download_file(pending_file)
            time.sleep(0.5)
        except Exception as err:
            logging.error("Faile to download: {}".format(pending_file), str(err))

if __name__ == '__main__':
    init_candidate_files()
    init_downloaded_files()
    calc_pending_download_file()
    download_files()