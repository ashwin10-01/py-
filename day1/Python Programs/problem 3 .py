a=int(input("Enter numbers: "))
b=int(input("Enter numbers: "))
c=int(input("Enter numbers: "))
d=list([a,b,c])
first=second=third=float('-inf')    
for i in d:
    if i > first:
        third=second
        second =first
        first= i
    elif i> second:
        third=second
        second=i
    else:
        third=i 
print("The first largest number is:",first,"\nthe second largest number is:",second,"\nthe third largest number is:",third  )

