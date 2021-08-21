import os
import logging
import zipfile

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
ARCHIVE_PATH = r'D:\data\edgar\enrich\s3'

downloaded_files = set()
total_files = set()

def get_files_in_zip(file):
    EDGAR_ZIP_FILE = os.path.join(ARCHIVE_PATH, file)
    EDGAR_ZIP = zipfile.ZipFile(EDGAR_ZIP_FILE)
    with open('d.txt','a') as downloaded:
        for file_name in EDGAR_ZIP.namelist():
            if file_name[-1:] == '/':
                continue
            downloaded.write('/Archives/' + file_name + '\n')


def parse_all_files():
    for zipf in os.listdir(ARCHIVE_PATH):
        get_files_in_zip(zipf)
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

def get_all_downloaded_files():
    # downloaded_files.update(parse_lines_in_file(r'd.txt'))
    # downloaded_files.update(parse_lines_in_file(r'D:\data\edgar\downloaded.txt'))
    downloaded_files.update(parse_lines_in_file(r'D:\data\edgar\files.bak'))
def get_total_files():
    total_files.update(parse_lines_in_file(r'D:\workspace\edgar-abs-kg\edgar_crawler\crawler-utils\invalid.txt'))

def get_to_be_downloaded_files():
    logging.info("Total files count: {}".format(len(total_files)))
    to_download_files = total_files - downloaded_files
    logging.info("Total pending files count: {}".format(len(to_download_files)))
    with open('pending.txt','a') as pending:
        for file_name in to_download_files:
            pending.write(file_name + '\n')

if __name__ == '__main__':
    get_all_downloaded_files()
    get_total_files()
    get_to_be_downloaded_files()