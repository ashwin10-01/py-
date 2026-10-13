def sum(a,b):
    return a + b
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = sum(numbers[0], numbers[1])
print("The sum of the first two numbers is:", result)