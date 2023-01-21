List = list(input())
upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijkmnopqrstuvwxyz")
PROOF = 0
proof = 0
if len(List) > 10000:
    quit()
else:
    for i in List:
        if i in upper:
            PROOF+=1
        if i in lower:
            proof+=1
    if PROOF == len(List):
        print("All Capital Letter")
    elif proof == len(List):
        print("All Small Letter")
    else:
        print("Mix")