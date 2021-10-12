from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

reg_row = r"(\+7|8){1}\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2})\s*\(*(\w{3}.)*\.*\s*(\d{4})*\)*"
sub_row = r"+7(\2)-\3-\4-\5 \6\7"

# TODO 1: выполните пункты 1-3 ДЗ
dict_phonebook = {}
for row in contacts_list:
  fio = ' '.join(row[0:2]).strip().split(' ')
  key = fio[0] + ' ' + fio[1]
  if key in dict_phonebook.keys():
    for v in range(3, 7):
      if dict_phonebook[key][v] == '':
        dict_phonebook[key][v] = row[v]
  else:
    dict_phonebook[key] = row
  for n in range(len(fio)):
    dict_phonebook[key][n] = fio[n]

for k, v in dict_phonebook.items():
  phone = re.sub(reg_row, sub_row, v[5])
  dict_phonebook[k][5] = phone.strip()

contacts_list = [i for i in dict_phonebook.values()]

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)
