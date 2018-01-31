def swap(i, j, arr):
	aux = arr[i];
	arr[i] = arr[j];
	arr[j] = aux;

def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] > arr[j]:
				swap(i, j, arr);

arr = [7, -3, 8, 0, 43, 3.14, -1.4, 1024, 25, 10]
bubblesort(arr);
for x in arr:
	print x;