def num(a):
    if a == 0:
        print("entered number is 0")
        return
    if a % 2 == 0:
        print("entered number is even")
    else:
        print("entered number is odd")

a = int(input("enter a number :"))
num(a)