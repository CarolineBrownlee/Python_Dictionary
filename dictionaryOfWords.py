# You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. You need to add a few more words and definitions to the dictionary.

# After you have added them, use square bracket notation to output the definition of two of the words to the console.

# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Running Gait"] = "How your foot strikes the ground."

word_definitions["Stride Length"] = "The distance from the toe of one foot to the toe of your other foot as you run."

word_definitions["Pronation"] = "The natural side-to-side movement of the foot as you walk or run."

""" 
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
for (key, value) in word_definitions.items():
    print(f"{value}")

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")

# print(word_definitions)