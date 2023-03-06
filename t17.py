# Enter your code here. Read input from STDIN. Print output to STDOUT


G = int(input())
for i in range(G):
    a = input()
    A_set = set(input().split())
    b = int(input())
    B_set = set(input().split())
    print(A_set.issubset(B_set))
