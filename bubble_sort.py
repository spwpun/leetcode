'''
冒泡排序
'''

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    return arr

arr = [1, 5, 3, 2, 4]
print(bubble_sort(arr))