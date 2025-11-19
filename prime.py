n=int(input('enter the number:'))
if n<=1:
    print(f'{n} is not prime')
elif n==2 or n==3:
    print(f'{n} is a prime')
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
             prime==False
             break
    if prime:
        print(f'{n} is a prime')
    else:
        print(f'{n} is not prime')
