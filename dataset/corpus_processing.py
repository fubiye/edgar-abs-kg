import pandas as pd
import re
CORPUS = r'D:\data\edgar\example\corpus.csv'

NOT_OPENNING_TAGS = set(['(',')','”',',','®'])
NOT_CLOSING_TAGS = set(['“','®'])
def format_content(content):
    content = ''.join([ line if line[0] in NOT_OPENNING_TAGS else '\n' + line  for line in content.split('\n') if len(line) > 0])
    content = ''.join([ line if line[-1:] in NOT_CLOSING_TAGS else line + '\n' for line in content.split('\n') if len(line) > 0])
    content = re.sub(' +', ' ',content)
    return content


if __name__ == '__main__':

    df = pd.read_csv(CORPUS)

    df['Content'] = df['Content'].apply(format_content)

    df.to_csv(CORPUS, index = False)