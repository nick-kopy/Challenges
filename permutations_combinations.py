'''
calculates the number of possible permutations or combinations
'''

from math import factorial

x = input('whole set? \n')

y = input('choosing how many? \n')

try:
    int(x)
    int(y)
except:
    print('please use positive integers')
    raise SystemExit

x = int(x)
y = int(y)

if x <= 0 or y <= 0:
    print('please use positive integers')
    raise SystemExit

if y > x:
    x, y = y, x
    print("I think you got those backwards, don't worry I know what you mean")

t = input('permutaiton or combination? type "p" or "c"? \n')

def permu(n, r):
    if n == r:
        return factorial(n)
    return int(factorial(n) / factorial(n-r))

def combi(n, r):
    if n == r:
        return 1
    return int(factorial(n) / (factorial(n-r) * factorial(r)))

if t == 'c':
    print(combi(x, y))
elif t == 'p':
    print(permu(x, y))
else:
    print('please just type one letter "p" or "c"')