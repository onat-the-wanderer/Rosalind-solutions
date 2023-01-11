#/Users/onat/Downloads/rosalind_dna-2.txt
def complementary(dna):
    pairs= {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"} #zip('ACGT', 'TGCA')
    cdna=[]
    for nuc in dna[::-1]:
        cdna.append(pairs[nuc])
    cdna="".join(cdna)
    file=open("result.txt","w+")
    file.write(cdna)
    file.close
    return print(cdna)

    
    
    
#/Users/onat/Downloads/rosalind_dna-2.txt
dir=input("type direction")
with open(dir,"r") as f:
    f=f.read().strip()
complementary(f)