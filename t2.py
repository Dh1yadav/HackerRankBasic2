if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
srt_arr = list(set(arr))
srt_arr.sort()
print(srt_arr[-2])
 
