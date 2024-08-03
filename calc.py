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
