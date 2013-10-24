f = open('rosalind_iev.txt', 'r')
groupings = map(int, f.readline().split())

prob = [2,2,2,1.5,1,0]

prob_tot = 0
i = 0

while i<len(groupings):
    prob_tot += prob[i]*groupings[i]
    i += 1

print prob_tot
