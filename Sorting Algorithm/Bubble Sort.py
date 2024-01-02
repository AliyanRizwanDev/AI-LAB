#EX 2.3

#Bubble Sort
def BubbleSort(arr):
     n = len(arr)
     for i in range(n):
         for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



print("Array:\n")
arr = ['M','O','H','S','I','N']
print(arr)
BubbleSort(arr)
print("Sorted Array:\n")
print(arr)
