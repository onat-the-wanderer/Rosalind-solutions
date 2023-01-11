def transcribing(dna):
    rna=dna.replace("T","U")
    file=open("result.txt","w+")
    file.write(rna)
    file.close()
    return print(rna)

dir=input("type direction")
with open(dir,"r") as f:
          f=f.read()

transcribing(f)


