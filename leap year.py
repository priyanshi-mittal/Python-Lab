n=int(input("Enter a year"))
if n%100==0:
    if n%400==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
elif n%4==0:
    print("leap year")
else:
    print("not leap year")
