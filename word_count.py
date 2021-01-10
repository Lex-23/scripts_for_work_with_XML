"""
Скрипт для подсчета числа строк и стоимости перевода текста на другой язык из xml файла
"""

import xml.etree.ElementTree as ET
import sys


# обрабатываемый файл
fname = sys.argv[1]

# стоимость перевода за 1 слово
k = sys.argv[2]


mytree = ET.parse(fname)
myroot = mytree.getroot()


# отсев повторяющихся строк
a = []
for x in myroot[0][0]:
    t = x.text
    a.append(t)
b = set(a)


# запись уникальных строк в текстовый файл для подсчета слов
f = open('test.txt', "w")
for i in b:
    f.write(i)
    f.write('\n')
f.close()


lines = 0
words = 0
letters = 0

for line in open('test.txt'):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print(f"unique strokes in the file: {lines}")
print(f'all cost this translate is {words * k} ')

"""python3 argv[0] argv[1]
Выше приведена команда для командной строки для подсчета стоимости перевода текста
argv[0] - путь к исполняемому файлу (или его имя, если вы находитесь в той же директории)
argv[1] - путь к файлу, который надо обработать (или его имя, если вы в той же директории)
argv[2] - стоимость перевода)
"""
