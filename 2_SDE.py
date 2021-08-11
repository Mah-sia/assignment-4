def SDE(a=float,b=float,c=float):
    from math import sqrt
    x1=(-b+sqrt(b*b-4*a*c))/2*a
    x2=(-b+sqrt(b*b-4*a*c))/2*a
    print('x1= ',x1,'and x2= ',x2)

SDE(1,0,-1)
