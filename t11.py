# Enter your code here. Read input from STDIN. Print output to STDOUT
e = input()
engl = set(map(int, input().split()))
f = input()
fren = set(map(int, input().split()))

final_set = engl.union(fren)
print(len(final_set))
