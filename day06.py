memo = dict()

def fibo_memo(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
        return memo[n]

def fibo_recursion(number: int) -> int:
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0

    elif number == 1:
        return 1
    else:

        return fibo_recursion(number - 1) + fibo_recursion(number - 2)


# n = int(input("Input number : "))
# for i in range(0, n):
#     print(i)
#     print(fibo_recursion(i))
n=int(input("?"))
print(fibo_recursion(n))
print(fibo_memo(n))
