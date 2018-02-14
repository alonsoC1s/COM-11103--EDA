
# coding: utf-8

# In[3]:

class Sorting:
    
    def swap(i, j, arr):
        aux = arr[i]
        arr[i] = arr[j]
        arr[j] = aux
    
    def bubblesort(arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    swap(i, j, arr)
    
    def __quicksort(l, r, arr) :
        if(l >= r):
            return
        idx = l
        swap(l, random.randint(l, r), arr);
        for i in range(l, r):
            if arr[i] < arr[r]:
                swap(i, idx, arr)
                idx = idx + 1
        swap(r, idx, arr)
        __quicksort(l, idx - 1, arr)
        __quicksort(idx + 1, r, arr)
    
    def quicksort(arr):
        quicksort(0, len(arr) - 1, arr)
        
    def selectionsort(arr):
        for i in range(len(arr)):
            j = i;
            while j > 0 and arr[j-1] > arr[j]:
                swap(j, j-1, arr)
                j = j - 1
    
    def mergesort(arr):
        if len(arr) == 1:
            return
        L = arr[0 : len(arr) / 2]
        R = arr[len(arr / 2), len(arr)]
        i = 0
        j = 0
        for idx in range(len(arr)):
            if j >= len(R) or (i < len(L) and L[i] < R[i]):
                arr[idx] = L[i]
                i = i + 1
            else:
                arr[idx] = R[j]
                j = j + 1
                
arr = [7, -3, 8, 0, 43, 3.14, -1.4, 1024, 25, 10]
Sorting.selectionsort(arr)
for x in arr:
    print (x);


# In[ ]:



