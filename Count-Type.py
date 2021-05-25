st = input()
wht = len(list(st.split()))-1
print('Whitespaces: ',wht)
st = st.lower()
vow=con=dig=0
for i in st:
    if i.isalpha():
        if i in 'aeiou':
            vow+=1
        else:
            con+=1
    if i.isdigit():
        dig+=1
print(f'No. of Vowels: {vow}\nNo. of Consonants: {con}\nNo. of digits: {dig}')
