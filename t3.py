if __name__ == '__main__':
    scr_onl = []
    both = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        both.append([name, score])
        scr_onl.append(score)
        
scr_onl.sort()
sec_min = 0
mini = scr_onl[0]
both.sort()

for i in scr_onl:
    if i != mini:
        sec_min = i
        break
    
for i in both:
    if i[1] == sec_min:
        print(i[0])
        

