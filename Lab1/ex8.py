

def howMany1(decimal):
    result=0;
    binary = str(bin(decimal))
    for i in binary:
        if '1'==i:
            result+=1
    return result


input=input("Enter a decimal number ")

print("In number", input, "are", howMany1(int(input)), "bits of 1")