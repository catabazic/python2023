
letters="qwertyuiopasdfghjklzxcvbnm"


def findLetter(letter, matrix):
    index=0
    for row in matrix:
        if letter == row[0]:
            return index
        index+=1
    return index

def createMatrix(string):
    matrix=[]
    for letter in string:
        if letter in letters:
            isHere=findLetter(letter,matrix)
            if isHere!=len(matrix):
                matrix[isHere][1]+=1
            else:
                row=[letter, 1]
                matrix.append(row)
    return matrix

def mostCommon(stringInput):
    string=stringInput.lower()
    number=0;
    result=""
    matrix=createMatrix(string)
    for row in matrix:
        if row[1]>number:
            result=row[0]
            number=row[1]
    return result


input=input("Enter a string: ")

print("The most common letter in your string is '", mostCommon(input), "'")





