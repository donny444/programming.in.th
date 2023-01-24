'''
num = [int(i) for i in input().split()]
three = list("ABCabc")
char = str(input(""))
'''
num = input("").split()
char = str(input(""))
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
for j in range(len(char)):
    if char[j] == "A" or "a":
        print(num[-1],end=" ")
    elif char[j] == "B" or "b":
        print(num[-2],end=" ")
    elif char[j] == "C" or "c":
        print(num[-3],end=" ")