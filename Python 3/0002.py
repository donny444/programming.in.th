'''
n = int(input("Enter amount of positive integer : "))
a = []
m = int()
M = int()
if(0<=n<=1000):
    for i in range(1,n):
        a[i-1] = int(input("Enter integer : "))
        if(-2000000000<=a[i-1]<=2000000000):
            if(a[i-1] <= m):
                m = a
            if(a[i-1] >= M):
                M =a
        else:
            break
'''
n = int(input("Enter amount of positive integer : "))
a = []
minBound,maxBound = -2000000000,2000000000

def maxNum(p):
    global maxBound
    if p < maxBound:
        maxBound = p
    if i == n-1:
        print(maxBound)

def minNum(p):
    global minBound
    if p > minBound:
        minBound = p
    if i == n-1:
        print(minBound)

for i in range(n):
    a.append(int(input("Enter positive integer : ")))
    p = a[i]
    maxNum(p)
    minNum(p)