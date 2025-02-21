
N, k = tuple(map(int,input().split()))
arr = [i for i in range(1, N+1)]
start = 0
dead_list=[]
while arr:
    kill = (start + (k-1)) % len(arr)
    dead = arr.pop(kill)
    dead_list.append(dead)
    start = kill

print('<', end='')
for ele in dead_list[:-1]:
    print(ele, end =', ')
print(f'{dead_list[-1]}>')