st = input()
ls = list(st.split())
nls = []
for i in ls:
    if i not in nls:
        nls.append(i)
    else:
        pass
print(*nls)
