
upper="QWERTYUIOPASDFGHJKLZXCVBNM"

def wordInLower(string):
    index=0
    modified_string=""
    for letter in string:
        if letter in upper:
            if index==0:
                modified_string+=string[index].lower()
            else:
                temp=string[index:]
                modified_string+="_"+temp[0].lower()+temp[1:]
        else:
            modified_string+=string[index]
        index+=1
    return modified_string

def UpperToLower(string):
    words=string.split()
    index=0
    for word in words:
        if word[0] in upper:
            for letter in word[1:]:
                if letter in upper:
                    words[index] = wordInLower(word)
                    break
        index+=1
    return " ".join(words)

input = input("enter a string: ")

print("You string in lower_case is: ", UpperToLower(input))




