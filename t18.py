strg = set(input().split())
N = int(input())
output = True

for i in range(N):
    strg2 = set(input().split())
    if not strg2.issubset(strg):
        output = False
    if len(strg2) >= len(strg):
        output = False

print(output)