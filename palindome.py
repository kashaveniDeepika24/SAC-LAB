s=input('enter a string:')
rev=""
for ch in s:
    rev=ch+rev
if s==rev:
    print('palindome')
else:
    print('not a palindome')
    
