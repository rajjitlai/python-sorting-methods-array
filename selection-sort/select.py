# Sorting Arrays using Selection Sort Method

def selSort(arr):
          n = len(arr)
          for i in range(n):
                    minId = i
                    for j in range(i+1, n):
                              if arr[j] < arr[minId]:
                                        minId = j
                              arr[i], arr[minId] = arr[minId], arr[i]

arr = [23, 56, 9, 103, 77]
selSort(arr)
print("Sorted array is: ", arr)
