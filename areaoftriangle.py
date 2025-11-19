import sys
import math
s1=float(sys.argv[1])
s2=float(sys.argv[2])
s3=float(sys.argv[3])
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-1)*(s-2)*(s-3))
print(f'area of the triangle:{area:.2f}')
