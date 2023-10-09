

def isPollindrom(number):
    reversed_number = str(number)[::-1]
    reversed_number = int(reversed_number)
    if reversed_number == number:
        return True
    else:
        return False


input=input("Enter a number to know if it is polindrom: ")

print("The number ", input, "is polindrom", isPollindrom(int(input)))