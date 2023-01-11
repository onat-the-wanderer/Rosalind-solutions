dir=input("type direction")
with open(dir,"r") as f:
          lines=[l.strip() for l in f.readlines()]
        
dict={}
label=""

for line in lines:
    if '>' in line:
        label=line
        dict[label]=""
    else:
        dict[label]+= line



def gc_content(seq):
    return round(((seq.count('C')+ seq.count('G')) / len(seq)) * 100,6)


resultdict={key: gc_content(value) for (key, value) in dict.items()}
maxgckey=max(resultdict, key=resultdict.get)

F= f'{maxgckey[1:]}\n{resultdict[maxgckey]}'

file=open("result.txt","w+")    
file.write(str(F))
file.close()