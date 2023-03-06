n,m = map(int, input().strip().split(' '))
array = list(map(int, input().strip().split(' ')))
s_happy_a = set(map(int, input().strip().split(' ')))
s_sad_b = set(map(int, input().strip().split(' ')))
happiness = 0
for i in array:
    if i in s_happy_a:
        happiness +=1
    elif i in s_sad_b:
        happiness -=1
print(happiness)
        
     
