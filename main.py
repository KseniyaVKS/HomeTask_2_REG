import re
from pprint import pprint
# Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_dic = {}
contacts = []

for contact in contacts_list:
    data = contact[3:]
    pattern = re.compile(r"(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?(доб.)?\s?(\d{4})?\)?")
    sub_pattern = r"+7(\2)\3-\4-\5 \6\7"
    correct_phone = pattern.sub(sub_pattern, data[2])

    data_new = []
    data_new += data[:2]
    data_new.append(correct_phone)
    data_new += data[3:]

    fio = ' '.join(contact[:3]).strip().split(' ')
    data_contact = fio + data_new
    if data_contact[0] not in contacts_dic:
        contacts_dic[data_contact[0]] = data_contact[1:]
    else:
        values = contacts_dic.pop(data_contact[0])
        contacts_dic[data_contact[0]] = [y if x == '' else x for x,y in zip(data_contact[1:], values)]

list = []
for key, values in contacts_dic.items():
    list = [key] + values
    contacts += [list]

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts)
