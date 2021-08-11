def MN_matris (n,m):#n=row and m=colums
    for i0 in range (1,n+1):
        for i1 in range (1,m+1):
            item=i1*i0
            print(item," ",end="")
        print ('\n') 

MN_matris(4,4)