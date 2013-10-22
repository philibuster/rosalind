f = open('rosalind_iprb.txt', 'r')
x,y,z = f.readline().split(' ')
k,m,n = int(x),int(y),int(z)
f.close()

def Mendl(k,m,n):
    i = (k*((k-1)+(2*m)+(2*n)))+(m*((0.75*(m-1))+n))
    t = k + m + n
    return i / t / (t - 1)

print Mendl(k,m,n)
