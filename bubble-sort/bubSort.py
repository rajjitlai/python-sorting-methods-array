# Sorting Arrays using Bubble Sort Method

def bubSort(arr):
          n = len(arr)
          for i in range(n):
                    for j in range(0, n-i-1):
                              if arr[j] > arr[j+1]:
                                        arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr = [4, 43, 22, 92, 78, 15, 50]
print("Before Sorting, the array is:", arr)

bubSort(arr)
print("After Sorting, the sorted array is:", arr)