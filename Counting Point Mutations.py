dir=input("type direction")
with open(dir,"r") as f:
          f=f.read().split("\n")


def num_point_mutations(f):
    num=0
    for i in range(len(f[0])):
        if f[0][i]!=f[1][i]:
            num +=1
    file=open("result.txt","w+")
    file.write(str(num))
    file.close()
    return 


num_point_mutations(f)