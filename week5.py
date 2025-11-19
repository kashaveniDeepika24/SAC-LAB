import math
def quadratic_roots(a,b,c):
    D=b**2-4*a*c
    if D>0:
        root1=(-b+math.sqrt(D))/(2*a)
        root1=(-b-math.sqrt(D))/(2*a)
        return 'real and distinct',(root1,root2)
    elif D==0:
        root=-b/(2*a)
        return 'real and equal',(root)
    else:
        real=-b/(2*a)
        img=math.sqrt(abs(D))/(2*a)
        return 'imaginary',(f'{real}+{img}i',f'{real}-{img}i')
a=float(input('enter coefficient of a:'))
b=float(input('enter coefficient of b:'))
c=float(input('enter coefficient of c:'))
nature,roots=quadratic_roots(a,b,c)
print('Nature of roots:',nature)
print('Roots:',roots)
