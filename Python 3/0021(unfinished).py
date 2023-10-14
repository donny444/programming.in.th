text = list(input("Enter Text: "));
vowels = ["a", "e", "i", "o", "u"];
encoded = "p";

for i in range(len(text)):
    for j in range(len(vowels)):
        if(text[i]==encoded and text[i-1]==vowels[j]):
            text.pop(i-1);
            #if(text[i+1]):
                #text.pop(i+1);
            #else:
                #continue;
        else:
            pass;

print(text);