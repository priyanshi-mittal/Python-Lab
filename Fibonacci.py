val1 =0
val2 =1
n = int(input("Enter number: "))
Sum = val1+val2
print(val1)
print(val2)
for i in range(n-2):
    val1 = val2
    val2 = Sum
    print(Sum)
    Sum = val2+val1
