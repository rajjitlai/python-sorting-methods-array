# Sorting Arrays using Insertion Sort Method

def insSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [1, 3, 6, 7, 4, 10]
insSort(arr)
print("Sorted array is:", arr)