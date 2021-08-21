import pandas as pd
import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'edgar',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
conn = pymysql.connect(**config)
sql = '''
 SELECT c.cik, c.company, c.loc, fi.id as filing_id, fi.filing as filing_type, fi.docs_link as idx_url, fi.filing_desc, fi.effective, fi.file_num, fi.file_num_raw, 
 f.seq as file_idx, f.description as file_desc, f.doc_name, f.doc_link, f.doc_type, f.size
 FROM edgar_company c
 left join edgar_company_filing fi on c.cik = fi.cik
 left join edgar_filing_file f on fi.id = f.filing_id
'''
df = pd.read_sql_query(sql, conn)
df.to_csv(r'D:\dataset\edgar\edgar_abs_universal.csv', index=None)