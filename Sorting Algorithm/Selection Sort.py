#EX 2.1
def selection_sort(arr):
     n = len(arr)
     for i in range(n):
         min_idx = i
         for j in range(i+1, n):
             if arr[i] < arr[j]:
                min_idx = j
                arr[i], arr[min_idx] = arr[j], arr[i]

     return arr



arr = [5,7,10]
sorted = selection_sort(arr)
print(sorted)