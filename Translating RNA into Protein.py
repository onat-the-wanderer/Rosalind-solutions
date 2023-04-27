#"/Users/onat/Downloads/rosalind_prot.txt"
dir=input("type directory")
with open(dir, "r") as f:
    f=f.read()

f=f[:-4] #this line is added in order to remove "NONE" characters at the end of protein sequence. will be reworked.

lib={
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
        'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
        'UAU':'Y', 'UAC':'Y', 'UAA':'', 'UAG':'',
        'UGU':'C', 'UGC':'C', 'UGA':'', 'UGG':'W',
        'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
        'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
        'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
        'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
        'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
        'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
        'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
    }

key_lib=list(lib.values())
print(key_lib)


def translation(rna):
    protein=""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        protein= protein + str(lib.get(codon)) 
    file=open("result.txt", "w+")
    file.write(protein)
    file.close
    print(len(protein))
    return print(protein)


translation(f)

