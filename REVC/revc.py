f = open('rosalind_revc.txt', 'r')
s = f.readline()
f.close()

def reverseDNA(string):
    x = list(string)
    t=0
    l=len(x)
    r=[]
    while t<len(x):
        if x[t] == 'A':
            r.append('T')
        elif x[t] == 'T':
            r.append('A')
        elif x[t] == 'C':
            r.append('G')
        elif x[t] == 'G':
            r.append('C')
        t+=1
    r =r[::-1]
    print ''.join(r)

reverseDNA(s)
