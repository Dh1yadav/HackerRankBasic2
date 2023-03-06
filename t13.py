# Enter your code here. Read input from STDIN. Print output to STDOUT

e = input()
eng = set(map(int, input().split()))
f = input()
fren = set(map(int, input().split()))

fin_set = eng.difference(fren)
print(len(fin_set))
