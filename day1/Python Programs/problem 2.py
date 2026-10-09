def check_number(num, value):
    if num == 0:
        print(f"{value} is zero")
    elif num % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

check_number(a, "a")
check_number(b, "b")    