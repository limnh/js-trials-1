"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 ==0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    # TODO: replace this line with your code
    result = []
    for i in range(0,len(items)):
        if i % 2 != 0:
            result.append(i)
    return result
    



def print_as_numbered_list(items):
    # TODO: replace this line with your code
    i = 1
    
    for item in items:
        print(f"{i}. {item}")
        
        i += 1


def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []
    
    for i in range(start,stop):
        if start < stop:
            start += 1
            nums.append(i)
    return nums


def censor_vowels(word):
    # TODO: replace this line with your code
    char = []
    
    for letter in word:
        if letter in 'aeiou':
            char.append('*')
        else:
            char.append(letter)
    return ''.join(char)



def snake_to_camel(string):
    # TODO: replace this line with your code
    camel_case = []
    for word in string.split("_"):
        camel_case.append(f'{word[0].upper()}{word[1:]}')
    return ''.join(camel_case)


def longest_word_length(words):
    # TODO: replace this line with your code
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)
            
    return longest


def truncate(string):
    # TODO: replace this line with your code
    result = []
    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)
    return ''.join(result)


def has_balanced_parens(string):
    # TODO: replace this line with your code
    parens = 0
    
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
            
        if parens < 0:
            return False
    return parens == 0


def compress(string):
    # TODO: replace this line with your code
    compressed = []
    current_char = ''
    char_count = 0
    
    for char in string:
        if char != current_char:
            compressed.append(current_char)
        
            if char_count > 1:
                compressed.append(str(char_count))

            current_char = char
            char_count = 0

        char_count += 1

    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)
