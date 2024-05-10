def toggle_characters(input_string):
    toggled_string = ""
    for char in input_string:
        if char.isalpha():
            toggled_string += char.swapcase()
        else:
            toggled_string += char
    return toggled_string
input_str = "Hello World 123"
toggled_str = toggle_characters(input_str)
print("Original string:", input_str)
print("Toggled string:", toggled_str)
