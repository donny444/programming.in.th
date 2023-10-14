lines = int(input("Enter N: "));

for i in range(lines):
    #print("-");
    for j in range(lines):
        print("-", end="");
        if(j == lines/2-1):
            print("*", end="");
    print("");
    #if(i==int(lines/2))