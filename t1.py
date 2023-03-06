if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
list_i = []
list_j = []
list_k = []
list_fin = []
    
list_i = [i for i in range(x+1)]
list_j = [j for j in range(y+1)]
list_k = [k for k in range(z+1)]

list_fin = [[i,j,k] for i in list_i for j in list_j for k in list_k if i+j+k!=n]

print(list_fin)
