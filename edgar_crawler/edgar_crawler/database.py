import pymysql
import configparser
import os

class Database():
    config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'abc123',
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

    
