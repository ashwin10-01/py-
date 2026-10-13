def big3(b):
    first = second = third = float('-inf')

    for i in b:
        if i > first:
            third = second
            second = first
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i

    print(
        "The first largest number is:", first,
        "\nThe second largest number is:", second,
        "\nThe third largest number is:", third
    )


b = list(map(int, input("Enter numbers separated by space: ").split()))
big3(b)
 

