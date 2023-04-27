def mendel():
    dir=input("type directory")
    with open(dir, "r") as f:
        (k,m,n)=(int(value) for value in f.readline().split())
    a=k+m+n
    num=(4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*a*(a-1))
    file=open("result.txt","w+")
    file.write(str(round(num,5)))
    file.close()

    return (print(round(num,5)))



mendel()


#/Users/onat/Downloads/rosalind_iprb.txt
