from HashTable import *


def insert(table, *args):
    for x in args:
        table.insert(x)


h = HashTable()
insert(h, 'Juan', 'Iñaki', 'Cabo', 'Carlos', 'Sigler')
print(h)