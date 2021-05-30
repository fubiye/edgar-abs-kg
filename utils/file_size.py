import pymysql
import configparser
import os
import numpy as np

class Database():
    config = {
            'host': '127.0.0.1',
            'port': 3306,
            'db': 'edgar',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
    }

    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read(os.path.join(os.path.expanduser('~'), 'database.ini'))
        for section in cfg:
            for key in cfg[section]:
                self.config[key] = cfg[section][key]
    def getConn(self):
        return pymysql.connect(**self.config)

if __name__ == '__main__':
    db = Database()
    conn = db.getConn()
    cursor = conn.cursor()
    
    result = {
        'KB': [],
        'MB': [],
        'GB': []
    }
    max_id = 0
    while True:
        cursor.execute('SELECT id, filing_desc FROM edgar_company_filing where id > {} limit 1000'.format(max_id))
        filingsRs = cursor.fetchall()
        if len(filingsRs) is 0:
            break
        for filingRs in filingsRs:
            id = filingRs['id']
            if id > max_id:
                max_id = id
            desc = filingRs['filing_desc']
            size = desc[desc.index('Size: ')+len('Size: '):]
            tokens = size.split(" ")
            if len(tokens) < 2:
                print('{} has issue'.format(id))
                continue
            try:
                result[tokens[1]].append(int(tokens[0]))
            except:
                print('id: {} size: {}'.format(id, size))
            
        print('max id is {}'.format(max_id))

    sizeSum = {
        'KB': np.array(result['KB']).sum(),
        'MB': np.array(result['MB']).sum(),
        'GB': np.array(result['GB']).sum()
    } 
    print(sizeSum)

