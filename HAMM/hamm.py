f = open('rosalind_hamm.txt', 'r')
s = f.readline()
s1 = f.readline()
f.close()

def hamdist(str1, str2):
    x = list(str1)
    y = list(str2)
    i = 0
    tot = 0
    while i<len(x):
        if x[i] != y[i]:
            tot += 1
        i += 1
    print tot

hamdist(s,s1)
