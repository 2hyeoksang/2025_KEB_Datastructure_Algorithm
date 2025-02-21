import time
import random

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e-s}')
        return r
    return wrapper


@time_decorator
def bubble_sort(arr):
    l_length = len(arr) - 1
    for i in range(l_length):
        t1 = True
        for j in range(l_length):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                t1 = False
                # print(j,end= ' ')
        if t1:
            return arr
    return arr

@time_decorator
def insert_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        while i > 0 and arr[i-1] > val:  # i > 0 조건이 없으면 아마 IndexError 날듯
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = val

    return arr


# @time_decorator   재귀함수 쓸 때는 조심
def quick_sort(arr):
    n = len(arr)
    if n <= 1 :
        return arr

    pivot = arr[n//2]
    left, mid, right = [], [], []

    for num in arr :
        if num < pivot :
            left.append(num)
        elif num > pivot :
            right.append(num)
        else:
            mid.append(num)

    return quick_sort(left) + mid + quick_sort(right)


arr1 = [random.randint(1,100000) for _ in range(10000)]
arr2 = arr1.copy()
arr3 = arr1.copy()

lists = [4,55,55,7,55,9,11]
print(quick_sort(lists))

print(bubble_sort(arr1))
print(insert_sort(arr2))
s = time.time()
print(quick_sort(arr3))
e = time.time()
print(f'실행시간 : {e-s}')