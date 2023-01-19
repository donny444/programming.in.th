
a = int(input("Enter a : "))
b = int(input("Enter b : "))
if((a>=1000000000)|(a<=0)|(b>=1000000000)|(b<=0)):
    print("Invalid value")
else:
    print("Summation equal to " + str(a+b))