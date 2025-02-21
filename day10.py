def bubble_sort(arr):
    l_length = len(arr) - 1
    for i in range(l_length):
        for j in range(l_length):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

print(bubble_sort([8, -11, 9, 1]))