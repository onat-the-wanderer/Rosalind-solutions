#"/Users/onat/Downloads/rosalind_subs-2.txt"
dir=input("type directory")
with open(dir, "r") as f:
    f=f.read()
       
f=f.split("\n")         # s, t = f.read().split()
string="".join(f[0])
substring="".join(f[1])
location=[]
locationasstring=""

def finding_motif(string):
    for i in range(len(string)):
        if string[i:].startswith(substring):
            location.append(i+1)
    file=open("result.txt", "w+")
    locationasstring="".join(str(location))
    locationasstring=locationasstring.replace("[","").replace("]", "").replace(",", " ")
    file.write(locationasstring)
    file.close      
    return 
    
finding_motif(string)
