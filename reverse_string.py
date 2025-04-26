def reverse_string(word):
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

text = "hello"
result = reverse_string(text)
print("Reversed string:", result)
