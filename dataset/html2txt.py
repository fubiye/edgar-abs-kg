import os
import logging
from bs4 import BeautifulSoup
import shutil
import re
NOT_STARTING_TAGS = set(['(','”',',',".","●",")","®",":"])

NOT_END_TAGS = set(['“',"●","■","(","—",'-',",",":"])
last_token = 'PLACEHOLDER'
PAGE_NO_PATTERN = re.compile(r'^([A-Z0-9]-)*[0-9]+$')
def is_not_start(token):
    global last_token
    last_end = last_token[-1]
    last_token = token
    if last_end in NOT_END_TAGS:
        return True
    if last_end.islower():
        return True

    if len(token) == 0:
        return False
    start = token[0]
    if last_end.isdigit() and not start.islower():
        return False

    if start in NOT_STARTING_TAGS:
        return True
    if start.islower():
        return True
    if len(token) > 2 and token[:2] == '“)':
        return True
    return False
def is_valid_token(token):
    if len(token) == 0:
        return False
    if PAGE_NO_PATTERN.match(token):
        return False
    return True
def parse_file(filing_file):
    logging.info("processing file: {}".format(filing_file))
    content = open(filing_file)
    html = ' '.join([line[:-1] for line in content.readlines()])
    soup = BeautifulSoup(html,features='lxml')
    # tables = soup.findAll("table")
    # if tables is not None:
    #     for table in tables:
    #         table.decompose()
    tokens = soup.findAll(text=True)
    tokens = [token.replace('\xa0','') for token in tokens]
    tokens = [token.strip() for token in tokens]
    tokens = [token for token in tokens if is_valid_token(token)]
    lines = ''.join([' ' + token if is_not_start(token) else ('\n' + token ) for token in tokens])
    return lines
def is_valid_line(line):
    tokens = line.split(" ")
    if len(tokens) < 10:
        return False
    return True
def format_text(text):
    text = text.replace("“","\"")
    text = text.replace("”","\"")
    text = text.replace("’", "'")
    return text
def process_text(text):
    lines = text.split('\n')
    lines = [line for line in lines if is_valid_line(line)]
    lines = [format_text(line) for line in lines]
    return '\n'.join(lines)
if __name__ == '__main__':
    # lines = parse_file(r'D:\data\edgar\sampling\Archives\edgar\data\802106\000153949715000287\n439_fwpx2.htm')
    lines = parse_file(r'D:/data/edgar/sampling/Archives/edgar/data/1013454/000153949715000034/n425_fwpx3.htm')
    text = process_text(lines)
    if not os.path.exists(r'D:/data/edgar/example/documents/1013454/000153949715000034'):
        os.makedirs(r'D:/data/edgar/example/documents/1013454/000153949715000034')
    with open(r'D:/data/edgar/example/documents/1013454/000153949715000034/n425_fwpx3.txt','w', encoding='utf-8') as f:
        f.write(text)
    