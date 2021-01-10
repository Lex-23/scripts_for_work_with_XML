"""
Скрип для сортировки строк в файле по одному из аттрибутов (задается вручную)
"""


import xml.etree.ElementTree as ET
import sys


# обрабатываемый файл
fname = sys.argv[1]

# задается параметр сортировки
prm = sys.argv[2]


# функция сортировки
def sortchildrenby(parent, attr):
    parent[:] = sorted(parent, key=lambda child: child.get(attr))


tree = ET.parse(fname)
root = tree.getroot()

sortchildrenby(root, prm)
for child in root[0]:
    sortchildrenby(child, prm)


# запись в новый файл уже отсортированной информации
tree.write('sorted.xml')


"""python3 argv[0] argv[1] argv[2]
Выше приведена команда для командной строки для подсчета стоимости перевода текста
argv[0] - путь к исполняемому файлу (или его имя, если вы находитесь в той же директории)
argv[1] - путь к файлу, который надо обработать (или его имя, если вы в той же директории)
argv[2] - параметр, по которому требуется провести сортировку
"""
