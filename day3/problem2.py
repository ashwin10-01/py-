a=input("Enter a string: ")
vowels=0
for i in a:
    if i in "aeiouAEIOU":
        vowels+=1
print("Number of vowels:",vowels)