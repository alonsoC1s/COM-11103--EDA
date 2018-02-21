import random


class Sorting:

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    def bubblesort(self, arr):
        comparisons = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                comparisons += 1
                if arr[j] < arr[i]:
                    self.swap(i, j, arr)
        return comparisons

    def __quicksort(self, l, r, arr):
        comparisons = 0
        if l >= r:
            return 0
        idx = l
        self.swap(l, random.randint(l, r), arr)
        for i in range(l, r):
            comparisons += 1
            if arr[i] < arr[r]:
                self.swap(i, idx, arr)
                idx += 1
        self.swap(r, idx, arr)
        comparisons += self.__quicksort(l, idx - 1, arr)
        comparisons += self.__quicksort(idx + 1, r, arr)
        return comparisons

    def quicksort(self, arr):
        return self.__quicksort(0, len(arr) - 1, arr)

    def selectionsort(self, arr):
        comparisons = 0
        for i in range(len(arr)):
            j = i
            comparisons += 1
            while j > 0 and arr[j] < arr[j-1]:
                self.swap(j, j-1, arr)
                j = j - 1
                comparisons += 1
        return comparisons

    def mergesort(self, arr):
        comparisons = 0
        if len(arr) == 1:
            return 0
        L = arr[0:int(len(arr)/2)]
        R = arr[int(len(arr)/2):len(arr)]
        comparisons += self.mergesort(L)
        comparisons += self.mergesort(R)
        i = 0
        j = 0
        for idx in range(len(arr)):
            comparisons = comparisons + 1
            if j >= len(R) or (i < len(L) and L[i] < R[j]):
                arr[idx] = L[i]
                i += 1
            else:
                arr[idx] = R[j]
                j += 1
        return comparisons