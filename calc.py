# 계산기
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide_free(a, b):
    return a/b 

def get_median(a, b):
    return (a+b)/2

def getSum_ver2(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i   
    return sum

def get_quotient(a, b):
    return a//b

def get_abs(num):
    if num >=0:
        return num
    else:
        return -num
    
def get_percentage(a, b):
    return (a/b) * 100

def get_sum_ver1(n):
    return n(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def testing():
    return 1