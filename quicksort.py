def swap(i, j, arr):
	aux = arr[i];
	arr[i] = arr[j];
	arr[j] = aux;

def quicksort(l, r, arr) :
	if(l >= r):
		return;
	idx = l;
	for i in range(l, r):
		if arr[i] < arr[r]:
			swap(i, idx, arr);
			idx = idx + 1;
	swap(r, idx, arr);
	quicksort(l, idx - 1, arr);
	quicksort(idx + 1, r, arr);

arr = [7, -3, 8, 0, 43, 3.14, -1.4, 1024, 25, 10]
quicksort(0, len(arr) - 1, arr);
for x in arr:
	print x;