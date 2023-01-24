number = []
setnum = {''}
for i in range(1,11,1):
    number.append(int(input("input number "+str(i)+": ")))
for x in number:
    setnum.add(x%42)
setnum.pop() #or setnum.remove('')
print(len(setnum))