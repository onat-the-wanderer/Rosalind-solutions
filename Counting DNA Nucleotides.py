def count_DNA_nucleotides(x):
    dict={}
    seq=[i for i in x]
    for nuc in seq:
        if nuc in dict:
            dict[nuc]+=1
        else:
            dict[nuc]=1
    result= [dict["A"], dict["C"], dict["G"], dict["T"]]
    a=str(result[0])
    b=str(result[1])
    c=str(result[2])
    d=str(result[3])
    file=open("result.txt","w+")
    file.write("{} {} {} {}\n" .format(a,b,c,d))
    file.close()
    
    return print(result[0],result[1],result[2],result[3])

dir=input("type directory")
with open(dir,"r") as f:
          f=f.read()

count_DNA_nucleotides(f)

#/Users/onat/Downloads/rosalind_dna-2.txt
