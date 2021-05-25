st = input()
ls = list(st.split())
ln = [len(q) for q in ls]
print('Longest word in the string: ',ls[ln.index(max(ln))])
print('Shortest word in the string: ',ls[ln.index(min(ln))])