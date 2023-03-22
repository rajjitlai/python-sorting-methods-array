# Sorting Arrays using Bubble Sort Method

def bubSort(arr):
          n = len(arr)
          for i in range(n):
                    for j in range(0, n-i-1):
                              if arr[j] > arr[j+1]:
                                        arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr = [5, 7, 1, 0, 6, 12, 11]
print("Before Sorting, the array is:", arr)

bubSort(arr)
print("After Sorting, the sorted array is:", arr)