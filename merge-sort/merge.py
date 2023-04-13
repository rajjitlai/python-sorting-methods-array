# Sorting Arrays using Merge Sort Method

def merge_sort(arr):
          if len(arr) > 1:
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
                    merge_sort(left_half)
                    merge_sort(right_half)
                    arr.clear()
                    while left_half and right_half:
                              if left_half[0] < right_half[0]:
                                        arr.append(left_half.pop(0))
                              else:
                                        arr.append(right_half.pop(0))
                    arr.extend(left_half or right_half)

numbers = [4, 3, 1, 0]
merge_sort(numbers)
print(numbers)
