
numbers="012345689"

def firstNumber(string):
    ok=0
    result=""
    for letter in string:
        if letter in numbers:
            result+=letter
            ok=1
        elif ok==1:
            break
    return result



input = input("Enter a string: ")

print("First number in your string is", firstNumber(input))

