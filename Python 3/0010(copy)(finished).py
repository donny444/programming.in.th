#Copied code
"""
mes = input("")
pos = 1


right  mid  left

  1     2     3


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
"""

sequences = input("");
position = 1;

for i in range(len(sequences)):
    if(sequences[i] == "A") and (position == 1):
        position = 2;
    elif(sequences[i] == "A") and (position == 2):
        position = 1;
    elif(sequences[i] == "A") and (position == 3):
        continue;
    elif(sequences[i] == "B") and (position == 1):
        continue;
    elif(sequences[i] == "B") and (position == 2):
        position = 3;
    elif(sequences[i] == "B") and (position == 3):
        position = 2;
    elif(sequences[i] == "C") and (position == 1):
        position = 3;
    elif(sequences[i] == "C") and (position == 2):
        continue;
    elif(sequences[i] == "C") and (position == 3):
        position = 1;
    else:
        break;

print(position);