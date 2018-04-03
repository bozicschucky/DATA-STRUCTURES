import sys
#old =sys.getrecursionlimit()
#sys.setrecursionlimit(1000000)
def fib1(n):
    """
    return pair of fibonacci numbers ,F(N) and F(N-1)
    """
    if n <=1:
        return(n,0)
    else:
        (a,b)=fib(n-1)
        return (a+b,a)
def fibA(num):
    """ In efficient fib number"""
    if num<3:
        return 1
    a=b=1
    for i in range(2,num):
        a,b=b,a+b
    return b

# def fibB(num):  #too slow
#     if num <3:
#         return [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597][num]
#     return fibB(num-1) + fibB(num-2)

def memoize(function):
    dict={}
    def wrapper(num):    #num comes from fibB(num)
        if num not in dict:
            dict[num] = function(num)
        return dict[num]
    return wrapper

def timer(function):
    from time import clock
    from sys import setrecursionlimit; setrecursionlimit(100)
#default=1000
    startTime=clock()
    def wrapper(*args,**kwargs):
        result = function(*args,**kwargs)
        return result
        elapsedTime = round(clock()-startTime,2)
        print('-->', function.__name__+"'s time='", elapsedTime,'seconds')
    return wrapper

@memoize
# @timer
def fibB(num):  #too slow
    if num <3: return 1
    return fibB(num-1) + fibB(num-2)

def fibC(num,dict):  #faster 57.11 seconds faster to 1000th
    if num in dict:                  #use memoization to improve speed in the program
        return dict[num]
    dict[num] = fibC(num-1,dict) + fibC(num-2,dict)
    return dict[num]

@timer
def fibG(num):
    from math import sqrt
    phi1=(1+sqrt(5))/2
    phi2=(1-sqrt(5))/2
    return round((phi1**num - phi2**num)/sqrt(5))

def fibGG(num):
    from decimal import Decimal,getcontext
    from math import sqrt
    if num >70:
        getcontext().prec=2*num
        phi1=(Decimal(1)+Decimal(5).sqrt(5))/Decimal(2)
        phi2=(Decimal(1)-Decimal(5).sqrt(5))/Decimal(2)
        return round((phi1**Decimal(num)-phi2**Decimal(num))/Decimal(5).sqrt())

print(fibG(70))
#print(fibB(70))




