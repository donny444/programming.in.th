dna1 = input("")
dna2 = input("")
same = ""
sameArray = []

if(len(dna1) >= len(dna2)):
    for i in range(len(dna1)):
        if(dna1[i] != "A" and dna1[i] != "C" and dna1[i] != "G" and dna1[i] != "T"):
            print("Only A, C, G, T")
        else:
            print("Okay")
else:
    for i in range(len(dna1)):
        if(dna1[i] != "A" and dna1[i] != "C" and dna1[i] != "G" and dna1[i] != "T"):
            print("Only A, C, G, T")
        else:
            print("Okay")
            if(len(dna1) >= len(dna2)):
                for i in range(len(dna2)):
                    if(dna2[i] == dna1[i]):
                        same += dna2[i]
                    else:
                        sameArray.append(same)
                        same = ""
            else:
                for i in range(len(dna1)):
                    if(dna1[i] == dna2[i]):
                        same += dna1[i]
                    else:
                        sameArray.append(same)
                        same = ""
#unfinished