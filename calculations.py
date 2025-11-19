def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return 'Error:ZeroDivisionError.'
print('math calculations')
a=int(input('enter first integer:'))
b=int(input('enter second integer:'))
print('addition:',add(a,b))
print('subtraction:',subtract(a,b))
print('multiplication:',multiply(a,b))
print('division:',divide(a,b))
