def sum(a,b):
    c = a + b
    print ("sum of two numbers is :",c)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sum(numbers[0], numbers[1])