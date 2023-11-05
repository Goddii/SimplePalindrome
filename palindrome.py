
def is_palindrome(string):
    string = string.replace(' ', '')
    reversed_string = string[::-1]

    return reversed_string

# get word from user
input_string = input('Please enter a string: ')
# reverse the word
print(f'The word {input_string} reversed is :',is_palindrome(input_string))