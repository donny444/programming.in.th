#Copied code
"""
number = []
setnum = {''}
for i in range(1,11,1):
    number.append(int(input("input number "+str(i)+": ")))
for x in number:
    setnum.add(x%42)
setnum.pop() #or setnum.remove('')
print(len(setnum))
"""
num = [];
diffnum = set();
for i in range(10):
    num.append(int(input("")));
for i in num:
    diffnum.add(i%42);
print(len(diffnum));