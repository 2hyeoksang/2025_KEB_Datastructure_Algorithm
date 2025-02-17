def is_even(num):
    if num % 2 == 0:
        return True
    return False

a=10    #0000 1010
b=11    #0000 1011  :   & => 0000 1010 , | => 0000 1011 , ^(NOR) => 0000 0001
# bit operation
print(a & b)
print(a | b)
print(a ^ b)

# n = int(input())
# print(is_even(n))
