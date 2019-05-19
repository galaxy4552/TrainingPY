import cs50

numbers = []

while True:

    number = cs50.get_int("Number: ")

    if not number:
        break

    if number not in numbers:
        numbers.append(number)

print()    
for number in numbers:
    print(number)
