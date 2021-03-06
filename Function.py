"""

Functions in python are defined by block keyword 'def'
def function_name (Formal parameter): # Function Definition
    Syntax_in_Python

function_name(Actual Parameter) # Function Call

What we passes is Actual parameter
What function receives is Formal parameter.

In General we never use the print statement in Function.

"""


def perfect(num):
    ls = []
    for q in range(1,num):
        if num%q==0:
            ls.append(q)
    if sum(ls) == num:
        return True
    else:
        return False


inp = int(input('Enter num: '))
print('Perfect Number') if perfect(inp) else print('Not Perfect')


def prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        from math import sqrt
        q = 2
        while q<=sqrt(num):
            if num % q==0:
                return False
        else:
            return True


inp = int(input('Enter num: '))
print('Prime Number') if perfect(inp) else print('Not Prime')


def Area_Rec(x,y):
    area = x*y
    return area


inp = input('Enter L<space>B: ')
l,b = map(int,inp.split())
print('Area of Rectangle: ',Area_Rec(l,b))


def Circ_fun(r):
    from math import pi
    peri = 2 * pi * r
    area = pi * r * r
    return area,peri


inp = int(input('Enter Radius: '))
A,P = Circ_fun(inp)
print(f'Perimeter {P} and Area of Circle {A}')


def pow_new(base,to_the):
    power = base**to_the
    return power


inp = input('Enter Base<space>Power: ')
b,p = map(int,inp.split())
print('Solution: ',pow_new(b,p))


def eligible(age):
    if age>=18:
        return True
    return False


inp = int(input('Enter Age: '))
A = eligible(inp)
print('Person is Eligible.') if A else print('Person in Ineligible.')


def eve_Check(num):
    if num & 1==1:
        return False
    return True


inp = int(input('Enter Number: '))
A = eve_Check(inp)
print('Even') if A else print('Odd')

