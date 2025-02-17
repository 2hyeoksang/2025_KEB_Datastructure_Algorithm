import numpy as np

narr = np.array([1,3.1,2,9])    #numpy는 C에 사용. 원소를 높은 type으로 다 변환시킴 float64 = double
#타입이 같아야 다루기 편하다
print(type(narr))
print(type(narr), type(narr[2]),type(narr[3]))
print(narr[0],narr[1],narr[2],narr[3])

array = [9,-11,8,7]
print(array[0],array[1],array[2],array[3])
print(id(array[0]),id(array[1]),id(array[2]),id(array[3]))
