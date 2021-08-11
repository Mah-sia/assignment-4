def LCM(a,b):
    len=a*b
    m_a=[]
    m_b=[]
    for i in range (0,len):
        x=int(a*i)
        m_a.append(x)
    print (m_a[:])
    for i in range (0,len):
        x=int(b*i)
        m_b.append(x)
    print (m_b[:])
    find=0
    for i1 in range (1,len):
        if find==0:
            for i2 in range (1,len):
                if m_a[i1]==m_b[i2]:
                    lcm=m_a[i1]
                    find=1
                    return lcm
        else:
            break
    
y=LCM(4,10)
print(y)
            

