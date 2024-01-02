#EX 2.3

#Insertion Sort
def InsertionSort(arr):
     for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key



print("Array:\n")
arr = ['M','O','H','S','I','N']
print(arr, end="\n")
InsertionSort(arr)
print("Sorted Array:\n")
print(arr)