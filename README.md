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
### LAB02
### Задание 1
![Картинка6](images/lab02/Ex01_min_max.png)
![Картинка7](images/lab02/Ex01_uniqsort.png)
![Картинка8](images/lab02/Ex01_flaten.png)
```python
def min_max(nums):
    if len(nums) == 0:
        return "ValueError"
    return (min(nums), max(nums))



def unique_sorted(nums):
    return sorted(set(nums))


def flatten(mat):
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            return 'TypeError'
        result.extend(item)
    return result
print('min_max:')
print(min_max([3, -1, 5, 5, 0]), min_max([42]), min_max([-5, -2, -9]), sep = '\n')
print(min_max([]), min_max([1.5, 2, 2.0, -3.1]), sep = '\n')
print('unique_sorted:')
print(unique_sorted([3, 1, 2, 1, 3]), unique_sorted([]), sep = '\n')
print(unique_sorted([-1, -1, 0, 2, 2]), unique_sorted([1.0, 1, 2.5, 2.5, 0]), sep = '\n')
print('flatten:')
print(flatten([[1, 2], [3, 4]]), flatten(([1, 2], (3, 4, 5))), flatten([[1], [], [2, 3]]), sep = '\n')
print(flatten([[1, 2], "ab"]))
```
### Задание 2
![Картинка9](images/lab02/Ex02_transpose.png)
![Картинка10](images/lab02/Ex02_row_sums.png)
![Картинка11](images/lab02/Ex02_col_sums.png)
```python
def transpose(mat):
    if len (mat) == 0:
        return []
    row_length = len(mat[0])
    if any(len(row) != row_length for row in mat):
        return "ValueError"
    return list(map(list, zip(*mat)))


def row_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    if any(len(row) != row_length for row in mat):
        return "ValueError"
    return [sum(row) for row in mat]


def col_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    if any(len(row) != row_length for row in mat):
        return "ValueError"
    return [sum(col) for col in list(zip(*mat))]

print('transpose:')
print(transpose([ [1, 2, 3] ]), transpose([ [1], [2], [3] ]), transpose([ [1, 2], [3, 4] ]), sep = '\n')
print(transpose([]), transpose([[1, 2], [3]]), sep = '\n')
print('row_sums:')
print(row_sums([ [1, 2, 3], [4, 5, 6] ]), row_sums([[-1, 1], [10, -10]]), sep = '\n')
print(row_sums([[0, 0], [0, 0]]), row_sums([[1, 2], [3]]), sep = '\n')
print('col_sums:')
print(col_sums([ [1, 2, 3], [4, 5, 6] ]), col_sums([[-1, 1], [10, -10]]), sep = '\n')
print(col_sums([[0, 0], [0, 0]]), col_sums([[1, 2], [3]]), sep = '\n')
```
### Задание 2
![Картинка12](images/lab02/Ex03_format_record.png)
```python
def format_record(rec):
    if not isinstance(rec, tuple) or len(rec) != 3:
        return 'TypeError'
    fio, group, gpa = rec
    gpa = f'{gpa:.2f}'
    fio = fio.strip()
    while '  ' in fio:
        fio = fio.replace('  ', ' ')
    lastname_N_O = [list(word) for word in fio.split()]
    lastname_N_O[0][0] = lastname_N_O[0][0].upper()
    lastname_N_O[1][0] = lastname_N_O[1][0].upper()
    if len(lastname_N_O)>2:
        lastname_N_O[2][0] = lastname_N_O[2][0].upper()
    form1 = "".join(lastname_N_O[0])
    form2 = "".join(lastname_N_O[1][0])
    if len(lastname_N_O) > 2:
        form3 = "".join(lastname_N_O[2][0])
        return f'{form1} {form2}. {form3}., {group} {gpa}'
    else:
        return f'{form1} {form2}., {group} {gpa}'

print(format_record(("Петров пётр", "IKBO-12", 5.0)))
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```