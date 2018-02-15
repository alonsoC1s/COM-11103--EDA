import random

class Movie:
    def __init__(self, id, year, name):
        self.id = id
        self.year = year
        self.name = name
        
    def __eq__(self, other):
        if self.id < other.id:
            return -1
        else:
            return 1
        
    def __str__(self):
        return "{" + self.id.__str__() + ", " + self.year.__str__() + ", " + self.name.__str__() + "}"


class Sorting:
    
    def swap(self, i, j, arr):
        aux = arr[i]
        arr[i] = arr[j]
        arr[j] = aux

    def bubblesort(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j].__eq__(arr[i]) < 0:
                    self.swap(i, j, arr)

    def __quicksort(self, l, r, arr) :
        if(l >= r):
            return
        idx = l
        self.swap(l, random.randint(l, r), arr);
        for i in range(l, r):
            if arr[i].__eq__(arr[r]) < 0:
                self.swap(i, idx, arr)
                idx = idx + 1
        self.swap(r, idx, arr)
        self.__quicksort(l, idx - 1, arr)
        self.__quicksort(idx + 1, r, arr)

    def quicksort(self, arr):
        self.__quicksort(0, len(arr) - 1, arr)

    def selectionsort(self, arr):
        for i in range(len(arr)):
            j = i;
            while j > 0 and arr[j].__eq__(arr[j-1]) < 0:
                self.swap(j, j-1, arr)
                j = j - 1

    def mergesort(self, arr):
        if len(arr) == 1:
            return
        L = arr[0 : int(len(arr)/2)]
        R = arr[int(len(arr)/2) : len(arr)]
        self.mergesort(L)
        self.mergesort(R)
        i = 0
        j = 0
        for idx in range(len(arr)):
            if j >= len(R) or (i < len(L) and L[i].__eq__(R[j]) < 0):
                arr[idx] = L[i]
                i = i + 1
            else:
                arr[idx] = R[j]
                j = j + 1


arr = [Movie(1, 2, 'gola'), Movie(2, 3, 'thoa'), Movie(-1, 5, 'gakj')]
Sorting().mergesort(arr)
for x in arr:
    print (x);
