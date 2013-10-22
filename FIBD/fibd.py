f = open('rosalind_fibd.txt', 'r')
n,k = f.readline().split()
x = int(n)
y = int(k)
f.close()

def rabbit(n,k):
    array = []
    for x in range(k-1):
        array.append(0)
    array.append(1)
    gen = 1
    while gen<n:
        new = 0
        for i in range(k-1):
            new = new + array[i]

        for i in range(k-1):
            array[i] = array[i+1]
        array[k-1] = new

        gen +=1
    print sum(array)


rabbit(x,y)
