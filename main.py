from pprint import pprint
import csv
import re

from data_file import pattern, substitution

with open("phonebook.csv", encoding="utf-8") as file:
    rows = csv.reader(file, delimiter=",")
    contact_list = list(rows)
    new_contact_list = []
    for i in contact_list:
        d = ' '.join(i[:3]).split(' ')
        new_contact_list.append(d[0:3] + i[3:7])
    for ph in new_contact_list:
        result = re.sub(pattern, substitution, ph[-2])
        ph[-2] = f"{result}"
    # pprint(new_contact_list)
    # cont_list = []
    for i in new_contact_list:
        for k in new_contact_list:
            if i[0] == k[0] and i[1] == k[1] and i is not k:
                if i[2] == '':
                    i[2] = k[2]
                if i[3] == '':
                    i[3] = k[3]
                if i[4] == '':
                    i[4] = k[4]
                if i[5] == '':
                    i[5] = k[5]
                if i[6] == '':
                    i[6] = k[6]
            cont_list = []
            for pok in new_contact_list:
                if pok not in cont_list:
                    cont_list.append(pok)
pprint(cont_list)

with open("New_phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(cont_list)
