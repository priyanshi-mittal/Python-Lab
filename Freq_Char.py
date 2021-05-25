st = input()
st = st.lower()
for i in 'abcdefghijklmnopqrstuvwxyz':
    if st.count(i):
        print(f'Frequence of {i} is {st.count(i)}.')
