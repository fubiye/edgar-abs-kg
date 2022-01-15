import re

text = '''
 (iv) ML-CFC
'''
print(re.split('\s\(([a-z]|[ivx]+|[0-9.]+)\)\s', text))
