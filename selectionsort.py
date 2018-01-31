def swap(i, j, arr):
	aux = arr[i];
	arr[i] = arr[j];
	arr[j] = aux;

def selectionsort(arr):
	for i in range(len(arr)):
		j = i;
		while j > 0 and arr[j-1] > arr[j]:
			swap(j, j-1, arr);
			j = j - 1;

arr = [7, -3, 8, 0, 43, 3.14, -1.4, 1024, 25, 10]
selectionsort(arr);
for x in arr:
	print x;