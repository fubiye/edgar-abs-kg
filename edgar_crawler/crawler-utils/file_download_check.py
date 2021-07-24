import zipfile
import pymysql

EDGAR_ZIP_FILE = r'/home/fubiye/storage/data/edgar/Archives_20210607_01_44.zip'
EDGAR_ZIP = zipfile.ZipFile(EDGAR_ZIP_FILE)

print("Start processing file: {}".format(EDGAR_ZIP_FILE))
compressed_files = set()
for file_name in EDGAR_ZIP.namelist():
    if file_name[-1:] == '/':
        continue
    compressed_files.add(file_name)

print("Total num of comparessed files: {}".format(len(compressed_files)))

print("Connecting to DB...")

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'edgar',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    'user': 'root',
    'password': 'abc123'
}

conn = pymysql.connect(**db_config)

QUERY_GET_FILING_FILES = "SELECT * FROM edgar_filing_file WHERE doc_type NOT IN ('GRAPHIC') and doc_link not like '%/'"
cursor = conn.cursor()
cursor.execute(QUERY_GET_FILING_FILES)
file_files_rs = cursor.fetchall()

db_files = set()
for rs in file_files_rs:
    db_files.add(rs['doc_link'])

print("Total num of DB files: {}".format(len(db_files)))

print("Start check downloaded files, please find invalid files below: ")
with open('invalid.txt','a') as invalid_file:
    for file in db_files:
        if file not in compressed_files:
            print(file)
            invalid_file.write(file + '\n')

