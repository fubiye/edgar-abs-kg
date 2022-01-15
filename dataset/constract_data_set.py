import pandas as pd
import zipfile
import os
import shutil

def select_data_set():
    df = pd.read_csv(r'D:\data\edgar\edgar_abs_universal.csv')
    df = df[(df['effective'] > '2020-01-01') & (df['effective'] < '2021-01-01')]
    df = df[~(df['company'].str.contains("auto", na=False, case=False))]
    df = df[~(df['doc_type'] == 'GRAPHIC')]
    df = df[~(df['doc_name'].str[-3:] == 'txt')]
    print(df)
    df.to_csv(r'D:\data\edgar\edgar_abs_2020.csv')

# def extract_file():
#     df = pd.read_csv(r'D:\data\edgar\edgar_abs_2020.csv')
    
def extract_the_file(zip_file_name, df):
    path = os.path.join(r'E:\dataset\edgar\enrich\s3',zip_file_name)
    if zip_file_name == 'Archives_20210607_01_44.zip':
        path = os.path.join(r'D:\data\edgar',zip_file_name)
    archieve = zipfile.ZipFile(path)
    df['file'].apply(lambda file: archieve.extract(file,r'D:\data\edgar\sampling\xml'))
    
def search_by_name(link, idx_df):
    data_file_name = '/'.join(link.split('/')[4:])
    print("processing: {}".format(data_file_name))
    matched = idx_df[idx_df['nfile'] == data_file_name]
    if len(matched) > 0:
        return matched.iloc[0][['file','zip']]
    return pd.Series({'file':None,'zip': None})
    # return pd.Series([link.split('/')[2],'/'.join(link.split('/')[4:])])
def match_in_archieve(df, idx_df):
    mapDf = pd.DataFrame()
    mapDf['doc_link'] = df['doc_link']
    mapDf[['file','zip']] = mapDf['doc_link'].apply(lambda link: search_by_name(link, idx_df))
    return mapDf
def nomalize_file_name(name):
    return '/'.join(name.split('/')[-3:])
def get_cik_from_nfile(nfile):
    tokens =  nfile.split('/')
    try:
        return int(tokens[0])
    except:
        try:
            return int(tokens[1])
        except:
            return -1

def query_file_to_extract():
    # df = pd.read_csv(r'D:\data\edgar\edgar_abs_2020-sample.csv')
    # idx_df = pd.read_csv(r'D:\data\edgar\file_index_sample.csv')
    df = pd.read_csv(r'D:\data\edgar\edgar_mbs_2020_company.csv')
    mbs_ciks = set(df['cik'])
    # df['cik'].apply(lambda cik: mbs_ciks.add(str(cik)))

    idx_df = pd.read_csv(r'D:\data\edgar\file_index.csv')
    idx_df.columns = ['file','zip']
    idx_df['nfile'] = idx_df['file'].apply(nomalize_file_name)
    idx_df['cik'] = idx_df['nfile'].apply(get_cik_from_nfile)
    print(len(idx_df))
    idx_df['match'] = idx_df['cik'].apply(lambda cik: True if cik in mbs_ciks else False)
    idx_df = idx_df[idx_df['match'] == True]
    # idx_df['match'] = idx_df['nfile'].apply(lambda nfile: True if ('htm' in nfile) and ('-index' not in nfile) else False)
    idx_df['match'] = idx_df['nfile'].apply(lambda nfile: True if '.xml' in nfile else False)
    idx_df = idx_df[idx_df['match'] == True]
    print(idx_df)
    # print(idx_df['cik'].unique())
    # df['nfile'] = df['doc_link'].apply(nomalize_file_name)
    # mapDf = match_in_archieve(df, idx_df)
    # df = pd.merge(df, idx_df,how='left')
    # print(idx_df)
    idx_df.to_csv(r'D:\data\edgar\map_xml_file_to_zip.csv',index=None)
def export_companies():
    df = pd.read_csv(r'D:\data\edgar\edgar_abs_2020.csv')
    companies = df[['cik','company']]
    companies = companies.drop_duplicates()
    companies.to_csv(r'D:\data\edgar\edgar_abs_2020_company.csv')
    print(companies)

def cleanup_by_cik():
    df = pd.read_csv(r'D:\data\edgar\edgar_mbs_2020_company.csv')
    mbs_ciks = set(df['cik'])
    to_delete = set()
    for cik in os.listdir(r'D:\data\edgar\sampling\Archives\edgar\data'):
        if not cik in mbs_ciks:
            to_delete.add(cik)
    print("Delete folder")
    for cik in to_delete:
        to_delete_path = os.path.join(r'D:\data\edgar\sampling\Archives\edgar\data',cik)
        print(to_delete_path)
        # shutil.rmtree(to_delete_path)     !!! delete all files
if __name__ == '__main__':
    # cleanup_by_cik()
    # select_data_set()
    # extract_the_file("edgar/data/1389368/000088237707000618/d637425.htm")
    # query_file_to_extract()
    with open('records.txt','r') as f:
        records = [line.split('\n')[0] for line in f]
    records = set(records)
    df = pd.read_csv(r'D:\data\edgar\map_xml_file_to_zip.csv')
    # print(df)
    by_zip = df[['file','zip']].groupby("zip")
    with open('records.txt','a') as f:
        for archieve, byZipDf in by_zip:
            print("{} - {}".format(archieve, len(byZipDf)))
            if archieve in records:
                print("skip: {}".format(archieve))
                continue
            extract_the_file(archieve, byZipDf)
            f.write(archieve + '\n')
    # print(df)