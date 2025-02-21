def bubble_sort(arr):
    l_length = len(arr) - 1
    for i in range(l_length):
        t1 = True
        for j in range(l_length):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                t1 = False
                print(j,end= ' ')
        if t1:
            return arr
    return arr

print(bubble_sort([8, -11, 9, 1]))
print(bubble_sort([1,2,3,4,5,6,7]))