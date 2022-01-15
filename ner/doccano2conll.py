# coding=utf-8
from pathlib import Path
import json
import re
def read_items():
    lines = Path(r'D:\dataset\edgar\cmbs_ner.jsonl').read_text(encoding='utf-8')
    return [eval(doc) for doc in lines.splitlines()]

def split_line_by_end(doc):
    data = doc['data']
    last_end = 0
    lines = []
    line = {
        'start': None,
        'end': None,
        'data': None,
        'label':[],
    }
    for label in doc['label']:
        if line['end'] is None or line['end'] < label[0]:
            if last_end > 0:
                lines.append(line)
                line = {
                    'start': None,
                    'end': None,
                    'data': None,
                    'label':[],
                }
            left = data.rindex("\n",last_end,label[0])
            right = data.index("\n",label[1],len(data))
            line['start'] = left+1
            line['end'] = right
            line['data'] = data[line['start']:line['end']]
            last_end = right
            line['label'].append([label[0]-line['start'],label[1]-line['start'],label[2]])
        else:
             line['label'].append([label[0]-line['start']-1,label[1]-line['start']-1,label[2]])
    return lines

def doc2lines(doc):
    lines = []
    lines_by_end = split_line_by_end(doc)
    tokens = []
    tags = []
    for line in lines_by_end:
        sublines = re.split('\s\(([a-z]|[ivx]+|[0-9.]+)\)\s', line['data'])
        if len(sublines) == 1:
            lines.append(line)
            continue
        
        curr_pos = line['start']
        for subline in sublines:
            if len(re.findall('^([a-z]|[ivx]+|[0-9.]+)$', subline)):
                curr_pos = curr_pos + len(subline)
                continue
            new_line = {
                'start': curr_pos,
                'end': curr_pos + len(subline),
                'data': subline,
                'label': []
            }
            for label in line['label']:
                if label[0] < new_line['start'] or label[1] > new_line['end']:
                    continue
                new_line['label'].append([label[0] - new_line['start'], label[1] - new_line['start'], label[2]])
            lines.append(new_line)
    return lines

def line2row(line):
    row = re.split(r"([\(\)\".。!！?？；;，,:：\s+])", line['data'])
    labels = ['O' for i in range(len(line['data']))]
    for label in line['label']:
        for i in range(label[0],label[1]):
            if i < 0:
                break
            labels[i] = label[2]
    
    last_label = 'O'
    curr_index = 0
    row_label = []
    for token in row:
        if curr_index > len(labels) - 1:
            break
        label = labels[curr_index]
        if label != 'O':
            if last_label == 'O':
                row_label.append('B-'+label)
            else:
                row_label.append('I-'+label)
        else:
            row_label.append('O')
        curr_index = curr_index + len(token)
        last_label = label
    
    tokens = []
    labels = []
    last_label = 'O'
    for idx in range(len(row)):
        token = row[idx]
        if token == '' or token == ' ':
            continue
        tokens.append(token)
        label = row_label[idx]
        if label[0] == "I" and last_label == 'O':
            label = 'B' + label[1:]
        labels.append(label)
        last_label = label

    return tokens, labels
if __name__ == '__main__':
    docs = read_items()
    with open('abs.conll','w',encoding='utf-8') as f:
        for doc in docs:
            lines = doc2lines(doc)
            for line in lines:
                tokens, labels = line2row(line)
                # print(line2row(lines[0]))
                for idx in range(len(tokens)):
                    f.write(f'{tokens[idx]}\t{labels[idx]}\n')
                f.write('\n')
            # break