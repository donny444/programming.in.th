String = str(input())
if len(String) > 10000:
    quit()
else:
    if String.isupper():
        print("All Capital Letter")
    if String.islower():
        print("All Small Letter")
    if String.isalpha() and not (String.isupper() or String.islower()):
        print("Mix")