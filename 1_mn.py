def MN_matris (n,m):
    for i0 in range (n):
        for i1 in range (m):
            if (i0%2==0 and i1%2==0) or (i0%2==1 and i1%2==1):
                print('*',end='')
            elif(i0%2==0 and i1%2==1) or (i0%2==1 and i1%2==0):
                print('#',end='')
        print ('\n')   

MN_matris(10,6)