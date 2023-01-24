min, max = -1000, 1000
confirm = False
while confirm == False:
    x1, s = [float(i) for i in input().split()]
    if(x1 >= min and x1 <= max) and (s >= min and s <= max):
        x2 = 2*s - x1
        print(x2)
        confirm = True
    else:
        print("Number must be in -1000 to 1000")