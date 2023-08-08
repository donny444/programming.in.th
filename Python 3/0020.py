sum = 0;
winner = None;
max = 0;
score = []

for i in range(5):
    rates = [int(x) for x in input().split()];
    for j in range(4):
        sum += rates[j];
    score.append(sum);
    sum = 0;

for i in range(5):
    if(score[i] > max):
        max = score[i];

for i in range(5):
    if(score[i] == max):
        winner = i+1;

print(winner, max);