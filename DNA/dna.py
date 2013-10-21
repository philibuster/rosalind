f = open('rosalind_dna.txt', 'r')
DNA = f.readline()
f.close()

def countDNA(x):
    a=c=g=t = 0
    s = list(x)
    length = 0
    while length<len(s):
        if s[length]=='A':
            a +=1
        elif s[length]=='C':
            c += 1
        elif s[length]=='G':
            g +=1
        elif s[length]=='T':
            t+=1
        length+=1
    print a,c,g,t

countDNA(DNA)
            
        
        
