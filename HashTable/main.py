from HashTable import *


def insert(table, *args):
    for x in args:
        table.insert(x)


h = HashTable()
insert(h, 'Juan', 'Iñaki', 'Cabo', 'Carlos', 'Sigler')
print(h)

checa = ["Cabo", "Cabito"]
for p in checa:
    print('It is ' + str(h.find(p)) + ' that ' + str(p) + ' is in the HashTable')