mes = input("")
pos = 1

"""
right  mid  left

  1     2     3

"""
for i in range(len(mes)):
   

    if (mes[i] == "A") and (pos == 1):
        pos = 2
    elif (mes[i] == "A") and (pos == 2):
        pos = 1
    elif (mes[i] == "A") and (pos == 3):
        pos = pos+0
    elif (mes[i] == "B") and (pos == 1):
        pos =pos+0
    elif (mes[i] == "B") and (pos == 2):
        pos = 3
    elif (mes[i] == "B") and (pos == 3):
        pos = 2
    elif (mes[i] == "C") and (pos == 1):
        pos = 3
    elif (mes[i] == "C") and (pos == 2):
        pos = pos + 0
    elif (mes[i] == "C") and (pos == 3):
        pos = 1
    else:
        break

print(pos)