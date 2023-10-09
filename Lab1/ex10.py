

def findWord(word, matrix):
    index=0
    for column in matrix:
        if word == column:
            return index
        index+=1
    return -1

def numberOfWords(string):
    string=string.lower()
    words=string.split()
    matrix=[]
    for word in words:
            isHere=findWord(word,matrix)
            if isHere!=-1:
                continue
            else:
                matrix.append(word)
    return len(matrix)


input=input("Enter a string: ")

print("The number of words in your string is ", numberOfWords(input))

