# 계산기
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide_premium(a, b):
    if b == 0:
        return("error!")
    return a/b 

def get_median(a, b):
    return (a+b)/2

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

