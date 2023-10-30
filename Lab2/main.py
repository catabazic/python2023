from collections import Counter


# -------------------------------Exercitiul 1
def Fibonaci(n: int):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return [0, 1]
    elif n > 2:
        result = [0, 1]
        a = 0
        b = 1
        for i in range(n - 2):
            c = a + b
            result.append(c)
            a = b
            b = c
        return result


# print("Fibonaci: ", Fibonaci(15))


# -------------------------------Exercitiul 2

def isPrime(n: int):
    if n < 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def checkListIfPrime(numbers: []):
    result = []
    for number in numbers:
        if isPrime(number):
            result.append(number)
    return result


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 17]


# print("Prime numbers are: ", checkListIfPrime(list))

# -------------------------------Exercitiul 3

def list_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    difference_a = set(a) - set(b)
    difference_b = set(b) - set(a)
    return intersection, union, difference_a, difference_b


# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection, union, difference_a, difference_b = list_operations(list_a, list_b)

# print(f"Intersection of a and b: {intersection}")
# print(f"Union of a and b: {union}")
# print(f"Difference of a - b: {difference_a}")
# print(f"Difference of b - a: {difference_b}")

# -------------------------------Exercitiul 4
def compose(notes, moves, start_position):
    song = []
    current_position = start_position
    song.append(notes[start_position])

    for move in moves:
        # Calculate the new position after applying the move
        current_position = (current_position + move) % len(notes)
        # Add the note at the new position to the song
        song.append(notes[current_position])

    return song


# Example usage
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2

result = compose(notes, moves, start_position)
#print(result)

# -------------------------------Exercitiul 5

def zero_below_diagonal(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Iterate through the matrix and set elements below the main diagonal to 0
    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0

    return matrix


# Example usage
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = zero_below_diagonal(input_matrix)
# print(result_matrix[0],"\n",result_matrix[1],"\n",result_matrix[2])

# -------------------------------Exercitiul 6


def find_items_with_x_occurrences(x, *args):
    # Count occurrences of items in each list
    item_counts = Counter()
    for lst in args:
        item_counts.update(lst)

    # Find items that appear exactly x times
    result = [item for item, count in item_counts.items() if count == x]

    return result


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]
list3 = [3, 4, 5, 6, 7]

x = 2
result = find_items_with_x_occurrences(x, list1, list2, list3)
#print(result)

# -------------------------------Exercitiul 7

def is_palindrome(number):
    # Convert number to string and check if it's equal to its reverse
    return str(number) == str(number)[::-1]


def find_palindromes(numbers):
    # Filter palindrome numbers from the list
    palindrome_numbers = [num for num in numbers if is_palindrome(num)]

    # Calculate the number of palindrome numbers and find the greatest palindrome number
    num_palindromes = len(palindrome_numbers)
    greatest_palindrome = max(palindrome_numbers) if palindrome_numbers else None

    return num_palindromes, greatest_palindrome


# Example usage
numbers = [121, 1331, 123, 454, 1001, 987]
num_palindromes, greatest_palindrome = find_palindromes(numbers)
# print(f"Number of palindromes: {num_palindromes}")
# print(f"Greatest palindrome number: {greatest_palindrome}")

# -------------------------------Exercitiul 8

def process_strings(x=1, strings=[], flag=True):
    result_lists = []

    for string in strings:
        filtered_chars = []
        for char in string:
            ascii_code = ord(char)
            if (ascii_code % x == 0) if flag else (ascii_code % x != 0):
                filtered_chars.append(char)
        result_lists.append(filtered_chars)

    return result_lists


# Example usage:
x = 2
strings = ["test", "hello", "lab002"]
flag = True
result = process_strings(x, strings, flag)
# print(result)

# -------------------------------Exercitiul 9

def find_unsatisfied_spectators(matrix):
    unsatisfied_spectators = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            height = matrix[i][j]
            can_see_game = True
            for k in range(i):
                if matrix[k][j] >= height:
                    can_see_game = False
                    break
            if not can_see_game:
                unsatisfied_spectators.append((i, j))
    return unsatisfied_spectators

# Example usage:
matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

unsatisfied_spectators = find_unsatisfied_spectators(matrix)
# print(unsatisfied_spectators)


# -------------------------------Exercitiul 10

def zip_lists(*args):
    max_length = max(len(lst) for lst in args)
    zipped_tuples = []

    for i in range(max_length):
        zipped_tuple = tuple(lst[i] if i < len(lst) else None for lst in args)
        zipped_tuples.append(zipped_tuple)

    return zipped_tuples

# Example usage:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = zip_lists(list1, list2, list3)
# print(result)


# -------------------------------Exercitiul 11

def sort_tuples(input_list):
    sorted_list = sorted(input_list, key=lambda x: x[1][2])
    return sorted_list

# Example usage:
input_list = [('abc', 'bcd'), ('abc', 'zza')]
sorted_result = sort_tuples(input_list)
# print(sorted_result)


# -------------------------------Exercitiul 12

def group_by_rhyme(words):
    rhymes_dict = {}

    for word in words:
        rhyme_key = word[-2:]
        if rhyme_key in rhymes_dict:
            rhymes_dict[rhyme_key].append(word)
        else:
            rhymes_dict[rhyme_key] = [word]

    grouped_rhymes = rhymes_dict.values()
    return grouped_rhymes


# Example usage:
words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print(result)
