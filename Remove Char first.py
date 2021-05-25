st1 = input()
st2 = list(input())
for i in st1:
    if i in st2:
        for q in range(st2.count(i)):
            st2.remove(i)
else:
    nst = ''
    for i in st2:
        nst+=i
    print(nst)
