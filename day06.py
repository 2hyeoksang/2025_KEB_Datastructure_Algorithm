#v1.4) v.07의 guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 문제도 지가 내고 지가 맞추고 (단, 해당 프로그램이 로그시간을 갖도록 한다.)

import random
a,b=1,1000
ans = random.randint(a,b)
chance = 10

def guess_num(a,b):
    return (a+b)//2

with open('guess.txt','w') as fp:
    while chance != 0 :
        guess = guess_num(a,b)
        print(f'C1 : "The Answer kis {guess}."')
        fp.write(f'Guess Number = {guess} / ')
        if guess == ans:
            print(f'C2 : "You Win. The Answer is {ans}."\n')
            fp.write(f'You Win. The Answer is {ans}\n')
            break
        elif guess < ans :
            chance -= 1
            print(f'C2 : "{guess} is lower. Left Chance : {chance}"\n')
            fp.write(f'{guess} is lower. Left Chance : {chance}\n')
            a = guess + 1
        elif guess > ans :
            chance -= 1
            print(f'C2 : "{guess} is bigger. Left Chance : {chance}"\n')
            fp.write(f'{guess} is bigger. Left Chance : {chance}\n')
            b = guess - 1

    else:
        print(f'C2 : "You lost. Answer is {ans}"\n')
        fp.write(f'You lost. The Answer is {ans}\n')