import itertools,sys

n = int(raw_input().strip())
letters = raw_input().strip().split(' ')

total = set(letters)
r= len(total)
query = ''.join(str(i) for i in range(1,n+1))
k = int(raw_input().strip())
required={}
required['a'] = []
for i in range(len(letters)):
    if letters[i]=='a':
        required['a'].append(str(i+1))



ans = itertools.combinations(query,2)
count_total = 0.0
match_count=  0
for a in ans:
    a = list(a)

    for elem in a:
        if elem in required['a']:

         match_count+=1
         break
    count_total+=1


print '%.3f' % float(match_count/count_total)