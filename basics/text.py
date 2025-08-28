s = 'test'
print(s)
s1 = len('test1')
print(s1)

s2 = s + ' ' + 'chandu'
print(s2)  # Concatenation (joining text)
print(s2 * 3)  # Repetition

word = 'Python'
print(word[3])  # Indexing (accessing a single character)

print(word[2:])  # Slicing (accessing a substring)
print(word[:2])  # Slicing from start to index 2 (not including index 2)

# String methods
text = "hello World"
print(len(text))  # Length of the string
print(text.upper())  # Convert to uppercase
print(text.lower())  # Convert to lowercase
print(text.replace("hello", "hi"))  # Replace substring
print(text.strip())  # Remove leading/trailing whitespace
print(text.startswith('h'))  # Check if string starts with a substring

# Iteration over string
for char in text:
    print(char)

# String formatting
name = "Alice"
age = 30
# Using f-strings (Python 3.6+)
print(f" My Name is{name}: and I am {age} years old.")

# Using str.format()
print("My Name is {}: and I am {} years old.".format(name, age))

# Using % operator
print("My Name is %s: and I am %d years old." % (name, age))

# Escape sequences
print("Hello\nWorld")  # Newline
print("Hello\tWorld")  # Tab
print("He said, \"Hello!\"")  # Double quote
print('It\'s a test.')  # Single quote
print("C:\\path\\to\\file")  # Backslash

# Unicode strings
print("नमस्ते")  # Hindi
print("こんにちは")  # Japanese
print("😊🚀")  # Emoji

# Checking text content
text1 = "Python3"
print(text1.isalpha())
print(text1.isdigit())
print(text1.isalnum())
print(text1.isspace())

#Multiline strings
msg = """Dear User,
This is a 
multiline message."""
print(msg)
