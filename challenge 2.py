import itertools,sys

n = int(raw_input().strip())
letters = raw_input().strip().split(' ')

total = set(letters)
r= len(total)
query = ''.join(str(i) for i in range(1,n+1))
k = int(raw_input().strip())




ans = itertools.combinations(query,k)
count_total = 0.0
match_count=  0
for a in ans:
    a = list(a)
    print a
    for elem in a:
        if letters[int(elem)-1]=='a':

         match_count+=1
         break
    count_total+=1


print '%.3f' % float(match_count/count_total)