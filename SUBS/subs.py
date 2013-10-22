f = open('rosalind_subs.txt','r').read()
s,t = f.split()

def find_all(a_str, sub):
    start = 0
    x=[]
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            break
        x.append(start+1)
        start += 1
    return '%s' % ' '.join(map(str, x))

print find_all(s,t)
