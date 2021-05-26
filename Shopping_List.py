print("Shopping List")
Sl = []
Q = []
while 1:
    inp = input().split()
    print(len(inp))
    print(inp[0])
    print(inp[1])
    q = inp[1]s
    if inp == '':
        break
    else:
        Sl.append(inp)
        Q.append(q)
print("-ShoppingList-")
o = [str(i) for i in Sl]
M = max(lambda x: len(x),o)
print(o)
print(M)
o2 = [str[i] for i in Q]
for q in range(len(Sl)):
    print(o[q].ljust(M)+'     '+o2[q].rjust[10])