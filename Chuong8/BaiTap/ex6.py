# Ex6
numbers = []

while True:
    value = input("Enter a number: ")
    if value.lower() == "done":
        break

    try:
        number = float(value)
        numbers.append(number)
    except ValueError:
        print("Invalid input")

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered.")