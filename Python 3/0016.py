adrianAnswer = "ABC"
brunoAnswer = "BABC"
goranAnswer = "CCAABB"
adrianPoint = 0
brunoPoint = 0
goranPoint = 0
N = int(input())
answer = str(input())
if N >= 0 and N <= 100:
    for i in range(N):
        if adrianAnswer[i%3] == answer[i]:
            adrianPoint += 1
        if brunoAnswer[i%4] == answer[i]:
            brunoPoint += 1
        if goranAnswer[i%6] == answer[i]:
            goranPoint += 1
    if adrianPoint > brunoPoint and adrianPoint > goranPoint:
        print(adrianPoint)
        print("Adrian")
    if brunoPoint > adrianPoint and brunoPoint > goranPoint:
        print(brunoPoint)
        print("Bruno")
    if goranPoint > adrianPoint and goranPoint > brunoPoint:
        print(goranPoint)
        print("Goran")