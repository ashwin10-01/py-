def vowels(a):
    count = 0
    for char in a:
        if char.lower() in 'aeiou':
            count += 1
    print("Number of vowels in the string:", count)

a = input("Enter a string: ")
vowels(a)