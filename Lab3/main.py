
#-------------------------------------Exerciutiul 1
def operate_lists(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_difference = set(a) - set(b)
    b_difference = set(b) - set(a)

    result_sets = [intersection, union, a_difference, b_difference]
    return result_sets


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = operate_lists(a, b)
#print(result)

#-------------------------------------Exerciutiul 2

def count_characters(text):
    char_count = {}  # Initialize an empty dictionary to store character counts

    # Iterate through each character in the input string
    for char in text:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            char_count[char] = 1

    return char_count


# Example usage:
input_string = "hello, world!"
result = count_characters(input_string)
#print(result)

#-------------------------------------Exerciutiul 3

def compare_dictionaries(dict1: dict, dict2: dict):
    # Check if the dictionaries have the same keys
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Iterate through key-value pairs and compare values recursively
    for key in dict1:
        if not compare_dictionaries(dict1[key], dict2[key]):
            return False
    return True


# Example usage:
dict1 = {
    'a': 1,
    'b': [2, 3, {'x': 4, 'y': 5}],
    'c': {'p': 6, 'q': [7, 8]}
}

dict2 = {
    'a': 1,
    'b': [2, 3, {'x': 4, 'y': 5}],
    'c': {'p': 6, 'q': [7, 8]}
}

dict3 = {
    'a': 1,
    'b': [2, 3, {'x': 4, 'y': 5}],
    'c': {'p': 6, 'q': [7, 9]}  # Different value in dict3 compared to dict1 and dict2
}

# print(compare_dictionaries(dict1, dict2))  # Output: True (dict1 and dict2 are equal)
# print(compare_dictionaries(dict1, dict3))  # Output: False (dict1 and dict3 are not equal)

#-------------------------------------Exerciutiul 4

def build_xml_element(tag, content, **kwargs):
    # Build the opening tag with tag name and attributes
    attributes = ' '.join([f'{key}="{value}"' for key, value in kwargs.items()])
    opening_tag = f'<{tag} {attributes}>' if attributes else f'<{tag}>'

    # Build the closing tag
    closing_tag = f'</{tag}>'

    # Construct the complete XML element
    xml_element = f'{opening_tag} {content} {closing_tag}'

    return xml_element


# Example usage:
result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
# print(result)

#-------------------------------------Exerciutiul 5

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            # If key is not in the dictionary, it doesn't match the rules
            return False
        value = dictionary[key]
        if not (value.startswith(prefix) and value.endswith(suffix) and middle in value and value.index(middle) > len(prefix) and value.index(middle) < len(value) - len(suffix)):
            # If the value does not match the rule, return False
            return False
    # All rules have been matched
    return True

# Example usage:
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key2": "start of winter", "key3": "this is not valid"}

result = validate_dict(rules, dictionary)
# print(result)  # Output: False


#-------------------------------------Exerciutiul 6

def count_unique_and_duplicates(input_list):
    unique_elements = set(input_list)
    num_unique = len(unique_elements)
    num_duplicates = len(input_list) - num_unique
    return num_unique, num_duplicates

# Example usage:
input_list = [1, 2, 2, 3, 4, 4, 5]
result = count_unique_and_duplicates(input_list)
# print(result)  # Output: (5, 2) (5 unique elements and 2 duplicate elements)


#-------------------------------------Exerciutiul 7

def set_operations(*args):
    result_dict = {}

    # Perform operations between sets two by two
    for i, set1 in enumerate(args):
        for j, set2 in enumerate(args):
            if i != j:
                union_key = f"{set1} | {set2}"
                intersection_key = f"{set1} & {set2}"
                difference_key1 = f"{set1} - {set2}"
                difference_key2 = f"{set2} - {set1}"

                # Calculate and store the results in the dictionary
                result_dict[union_key] = set1 | set2
                result_dict[intersection_key] = set1 & set2
                result_dict[difference_key1] = set1 - set2
                result_dict[difference_key2] = set2 - set1

    return result_dict


# Example usage:
set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)

# Print the results
# for key, value in result.items():
#     print(f"{key}: {value}")

#-------------------------------------Exerciutiul 8

def loop(mapping):
    visited = set()  # Set to keep track of visited keys
    result = []
    current_key = mapping.get('start', None)  # Get the initial key 'start'

    while current_key is not None and current_key not in visited:
        result.append(current_key)
        visited.add(current_key)
        current_key = mapping.get(current_key, None)  # Get the next key based on the current key

    return result

# Example usage:
mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
# print(result)  # Output: ['a', '6', 'z', '2']



#-------------------------------------Exerciutiul 9


def count_matching_arguments(*args, **kwargs):
    # Get the values from keyword arguments
    keyword_values = set(kwargs.values())

    # Count the number of positional arguments whose values are in keyword arguments
    count = 0
    for arg in args:
        if arg in keyword_values:
            count += 1

    return count


# Example usage:
result = count_matching_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5)
# print(result)  # Output: 3 (values 1, 2, and 3 are present among keyword arguments values)
