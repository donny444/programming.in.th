num = int(input())
mooksArray = []
for i in range(num):
    mook = input("")
    if(len(mooksArray) == 0):
        mooksArray.append(mook)
    else:
        for j in range(len(mooksArray)):
            if(mook == mooksArray[i]):
                break
            else:
                continue
        else:
            mooksArray.append(mook)

for i in range(len(mooksArray)):
    print(mooksArray[i])

#unfinished