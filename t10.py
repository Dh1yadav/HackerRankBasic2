# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c = list(map(str, input().split()))
    if c[0] == "pop":
        s.pop()
    elif c[0] == "remove":
        try:
            s.remove(int(c[1]))
        except:
            continue
    elif c[0] == "discard":
        try:
            s.discard(int(c[1]))
        except:
            continue
print(sum(s))
