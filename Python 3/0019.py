n = int(input("Enter N: "));
S = 1;
B = 0;
for i in range(n):
    s, b = input("Enter S B: ").split();
    S *= int(s);
    B += int(b);
if(S > B):
    print(S-B);
if(B > S):
    print(B-S);