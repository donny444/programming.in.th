'''
a = []
for i in range(2):
    a.append(int(input()))
print(a)
'''
a = [[],[]]
m = int(input())
n = int(input())
if(m>=1&n<=100):
    for i in range(m*n):
        a[0].append(int(input()))
    for j in range(m*n):
        a[1].append(int(input()))
    for k in range(m*n):
        print(str(a[0][k-1] + a[1][k-1]) + " ")
        if((k+1)%3==0):
            print("\n")