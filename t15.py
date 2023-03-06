# Enter your code here. Read input from STDIN. Print output to STDOUT

in_p = int(input())
set_og = set(map(int, input().split()))
gvn_int = int(input())

for i in range(gvn_int):
    oprt = input().split()
    if oprt[0] == 'intersection_update':
        set_t = set(map(int, input().split()))
        set_og.intersection_update(set_t)
    elif oprt[0] == 'update':
        set_t = set(map(int, input().split()))
        set_og.update(set_t)
    elif oprt[0] == 'symmetric_difference_update':
        set_t = set(map(int, input().split()))
        set_og.symmetric_difference_update(set_t)
    elif oprt[0] == 'difference_update':
        set_t = set(map(int, input().split()))
        set_og.difference_update(set_t)
    else:
        assert False
print(sum(set_og))
            
    
