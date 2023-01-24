number = []
total = 0
for x in range(9):
    number.append(int(input("")))
    total += number[x]
#print(total)
#print(number)
for i in range(9):
    if len(number) != 7:
        for j in range(9):
            if total-int(number[i])-int(number[j]) == 100:
                #print(number[i],number[j])
                number.pop(i)
                number.pop(j-1)
                break
            else:
                pass
    elif len(number) == 7:
        break
for num in number:
    print(num)