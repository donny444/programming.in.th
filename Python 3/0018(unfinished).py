import math;

n = int(input("Enter N: "));
k = int(input("Enter K: "));
p = None;

list = [];

for i in range(2, n+1):
    list.append(i);

def notPrime(num):
    if(num <  2):
        return True;
    if(num == 2):
        return True;
    if(num % 2 == 0):
        return True;
    for j in range(3, int(math.sqrt(num+1)), 2):
        if(num % j == 0):
            return True;
    return False;

for i in list:
    if(notPrime(i)):
        list[i] = None;

for i in list:
    if(list[i] != None):
        p = list[i];

print(n);
print(k);
print(p);