#dir=input("type directory")
dir="/Users/onat/Downloads/rosalind_subs.txt"
with open(dir, "r") as f:
    f=f.read()
       
f=f.split("\n")   
string="".join(f[0])
substring="".join(f[1])
location=[]

def finding_motif(string):
    for i in range(len(string)):
        if string[i:].startswith(substring):
            location.append(i+1)
    file=open("result.txt", "w+")
    file.write("".join(str(location)))
    file.close      
    return 
    
finding_motif(string)


