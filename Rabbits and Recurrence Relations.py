def rabbits_number(n,k):
    Fn=1
    Fm=1
    for mounths in range(2,n):
        F= Fn + k*Fm
        Fm=Fn
        Fn=F
    file=open("result.txt","w+")
    file.write(str(F))
    file.close()
    return print(F)
        
dir=input("type direction")
with open(dir,"r") as f:
          f=f.readline().strip().split(" ",2)
        
rabbits_number(int(f[0]),int(f[-1]))

#/Users/onat/Downloads/rosalind_fib-4.txt