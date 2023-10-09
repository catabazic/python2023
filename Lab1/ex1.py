import math

def gcd_multiple(numbers):
    result = int(numbers[0])
    for num in numbers[1:]:
        result = math.gcd(result, int(num))
    return result

while True:
    numbers= input("Enter a list of numbers separated by space: ").split()
    if len(numbers)<2:
        print("You should enter more than 2 numers")
    else :
        greatest_divisor = gcd_multiple(numbers)

        print("The greatest divisor of", numbers, "is", greatest_divisor)
        break

