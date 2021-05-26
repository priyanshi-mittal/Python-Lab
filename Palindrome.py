inp = input()
for i in range(len(inp)//2):
    if inp.find(inp[i]) == len(inp) - 1 - inp.rfind(inp[i]):
        print(f'case {i} runs.')
    else:
        print("Not Palindrome.")
        break
else:
    print('Palindrome.')
