
def count_occurrences(first_string, second_string):
    count = 0
    i = 0

    while i < len(second_string):
        # Find the next occurrence of first_string in second_string
        index = second_string.find(first_string, i)

        if index == -1:
            break
        # Increment count and move the index to the next position after the occurrence
        count += 1
        i = index + 1

    return count

firstString = input("Enter first string: ")
secondString = input("Enter second string: ")

occurrences = count_occurrences(firstString, secondString)
print("The number of occurrences of '",firstString,"' in '",secondString,"' is: ", occurrences)