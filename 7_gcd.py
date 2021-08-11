def gcd(x,y):
    if(x<y):
        temp=x
        x=y
        y=temp
    for i in range (0,y):
        if y!=0:
            r=x%y
            x=y
            y=r
        else:
            break
    r=x
    return r
    

gcd1=gcd(12,30)
print(gcd1) 
