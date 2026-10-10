a=list(map(int, input("Enter numbers separated by space: ").split()))
sum=0
even=0
b=(a)
for i in a:
    sum+=i
    if i%2==0:
        even+=1 
    if a.count(i) > 1:
        b.remove(i)
        
print("Sum of numbers:",sum)
print("Count of even numbers:",even)
print("List after removing duplicates:",b)
