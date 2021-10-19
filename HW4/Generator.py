import hashlib


def convert_md5(path='iterator.txt'):
    with open(path, 'r', encoding='utf-8') as file:
        for text in file:
            yield hashlib.md5(text.strip().encode('utf-8')).hexdigest()


for i in convert_md5():
    print(i)
