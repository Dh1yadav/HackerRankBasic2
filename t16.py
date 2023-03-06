# Enter your code here. Read input from STDIN. Print output to STDOUT

No_fam = int(input())
no_r = map(int, input().split(' '))
s_no_r = sorted(no_r)

for i in range(len(s_no_r)):
    if(i!=len(s_no_r)-1):
        if s_no_r[i]!=s_no_r[i-1] and s_no_r[i]!=s_no_r[i+1]:
            print(s_no_r[i])
            break;
    else:
        print(s_no_r[i])
