from HashTable import *


def insert(table, *args):
    for x in args[0]:
        table.insert(x)


file = open('Keywords.txt', 'r')
palabras = file.read().split('\n')
h = HashTable()

for p in palabras:
	h.insert(p)

print(h)

checa = ["Cabo", "Cabito"]
for p in checa:
    print('It is ' + str(h.find(p)) + ' that ' + str(p) + ' is in the HashTable')