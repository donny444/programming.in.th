n = int(input())
p = []
max = 0

for i in range(n):
    x, y = input().split()
    p.append([int(x), int(y)])

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            area = abs((p[i][0]*p[j][1])+(p[j][0]*p[k][1])+(p[k][0]*p[i][1])-(p[i][1]*p[j][0])-(p[j][1]*p[k][0])-(p[k][1]*p[i][0]))/2
            if(area > max):
                max = area

print(max)