a,b = [int(e) for e in input("").split()]
i = 1
total = 0
while i <= a or i <= b:
    if a%i==0 and b%i==0:
        x=i
    i += 1
print(x)