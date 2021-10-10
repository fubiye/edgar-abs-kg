import pandas as pd

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

df = pd.read_csv(r'D:\data\edgar\abs-company.csv')
ciks = set(parse_lines_in_file('cik.txt'))
# print(ciks)
df['exist'] = df['cik'].apply(lambda cik: 'Y' if str(cik) in ciks else None)
df.dropna(inplace=True)
# print(type(df.iloc[0].cik))
df.to_csv(r'D:\data\edgar\abs-company-since-2015.csv')