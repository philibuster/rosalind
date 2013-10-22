f = open('rosalind_gc.txt', 'r')
raw_samples = f.readlines()
f.close()

arr = {}
current = ''

for elem in raw_samples:
    if elem[0] == '>':
        current = elem[1:].rstrip()
        arr[current] = ''
    else:
        arr[current] += elem.rstrip()

for s_id, s in arr.iteritems():
    arr[s_id] = (float(s.count('G') + s.count('C'))/len(s))*100

(s_id, gc) = max(list(arr.iteritems()), key = lambda item:item[1])
print s_id
print gc
