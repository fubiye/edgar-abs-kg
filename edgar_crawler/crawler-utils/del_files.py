import os
import shutil

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

del_files = parse_lines_in_file('delete_ciks.txt')
for del_file in del_files:
    f = os.path.join(r'D:\dataset\edgar\temp\data', del_file)
    if os.path.exists(f):
        print('deleting: {}'.format(f))
        shutil.rmtree(f)