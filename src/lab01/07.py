st = str(input())
ans = ""
step = []
k = 0
k1 = 0
k2 = 0
for a in st:
    k += 1
    if a.isupper():
        l = st.find(a)
        st = st[l:]
        ans += a
        k1 = k
    elif a.isdigit():
        k2 = k
        step.append(k2 - k1 + 1)
        rstep = min(step)

for i in range(0, len(st), rstep):
    print(st[i])
