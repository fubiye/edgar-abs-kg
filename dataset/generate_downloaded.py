import os
BASE_DIR = r'D:\data\edgar\sampling\Archives\edgar\data'

def generate_downloaded_files():
    with open('mbs-downloaded.txt','w') as f:
        for cik in os.listdir(BASE_DIR):
            for accessionNum in os.listdir(os.path.join(BASE_DIR, cik)):
                for fileName in os.listdir(os.path.join(BASE_DIR, cik, accessionNum)):
                    f.write('/Archives/edgar/data/'+ cik +'/' + accessionNum + '/' + fileName + '\n')
def generate_cik_index_json():
    with open('mbs-index.txt','w') as f:
        for cik in os.listdir(BASE_DIR):
            longCik = cik.rjust(10,'0')
            f.write('https://data.sec.gov/submissions/CIK'+ longCik +'.json\n')
if __name__ == '__main__':
    generate_cik_index_json()
