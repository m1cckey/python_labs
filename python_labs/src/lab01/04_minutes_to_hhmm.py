res = int(input())
k = 0
while res > 60:
    res -= 60
    k+=1
print(f'{k}:{res}')