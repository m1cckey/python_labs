# python_labs
### LAB01
### Задание 1
![Картинка1](images/lab01/img01_Ganeev_lenar.png.png)
```python


name = input()
age = int(input())
print (f'Привет,{name}! через год тебе будет {age+1} ' )
```
### Задание 2
![Картинка2](images/lab01/img02_Ganeev_Lenar.png.png)
```Python


num = list(map(float, input().split()))
print(sum(num), f'{sum(num)/2:.2f}')
```
### Задание 3
![Картинка3](images/lab01/img03_Ganeev_Lenar.png.png)
```Python


price, discount, vat = map(int, input().split())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'{base :.2f}')
print(f'{vat_amount :.2f}')
print(f'{total :.2f}')
```
### Задание 4
![Картинка4](images/lab01/img04_Ganeev_Lenar.png.png)
```Python


res = int(input())
k = 0
while res > 60:
    res -= 60
    k+=1
print(f'{k}:{res}')
```
### Задание 5
![Картинка5](images/lab01/img05_Ganeeev_Lenar.png.png)
```Python

st = str(input())
ini = ''
while '  ' in st:
    st = st.replace('  ', ' ')
st = st.strip()
for a in st:
    if a.isupper():
        ini += a


print(ini)
print(len(st))
```
### Задание 7
```python
st = str(input())
ans = ''
step = []
k = 0
k1 = 0
k2 = 0
for a in st:
    k+=1
    if a.isupper():
        l = st.find(a)
        st = st[l:]
        ans += a
        k1 = k
    elif a.isdigit():
        k2 = k
        step.append(k2-k1+1)
        rstep = min(step)

for i in range(0,len(st), rstep):
    print(st[i])
```