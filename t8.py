# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
Mls = set(map(int, input().split(' ')))
N = int(input())
Nls = set(map(int, input().split(' ')))

op_set = Mls.difference(Nls)
oq_set = Nls.difference(Mls)
finl_set = op_set.union(oq_set)
finl_set = sorted(finl_set)

for i in finl_set:
    print(i)
