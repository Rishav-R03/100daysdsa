spam = 1
text = "# this is not a comment because it's inside quotes."
# This is a comment
'''
    Multi-line comment
'''
print('doesn\'t work') #\ used for escaping the single quote
# '\n' means newline

text = "Python is fun!"
print(text[0])
print(text[7])
print(text[-2])

rgb = ["red", "green", "blue"]
rgba = rgb
print(id(rgb) == id(rgba))