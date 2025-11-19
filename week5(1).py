def fibonacci(n):
    '''nth term in fibonnaci series'''
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input('enter n:'))
print(f'{n}th term in fibonacci series is:',fibonacci(n))
