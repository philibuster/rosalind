f = open('rosalind_rna.txt', 'r')
DNA = f.readline()
f.close()

def makeRNA(string):
    x = list(string)
    t = 0
    while t<len(x):
        if x[t]=='T':
            x[t]='U'
        t+=1
    ans = ''.join(x)
    print ans

makeRNA(DNA)
