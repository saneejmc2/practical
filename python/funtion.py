# Function Arguments in Python
#1.Positional Arguments
#2.Keyword Arguments
#3.Default Arguments
#4.Variable-length Arguments
#5.Arbitrary positional Arguments
#6.Arbitrary keyword Arguments

#1. Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
print("**Positional Arguments:")
greet("Alice", 30)  # Output: Hello Alice, you are 30 years old.

#2. Keyword Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")   
print("**Keyword Arguments:") 
greet(age=30, name="Alice")  # Output: Hello Alice, you are 30 years old.

#3. Default Arguments
def greet(name, age=25):
    print(f"Hello {name}, you are {age} years old.")
print("**Default Arguments:")
greet("Alice")  # Output: Hello Alice, you are 25 years old.
greet("Bob", 30)  # Output: Hello Bob, you are 30 years old.

#4. Variable-length Arguments
def greet(*names):
    for name in names:
        print(f"Hello {name}!")
print("**Variable-length Arguments:")
greet("Alice", "Bob", "Charlie")
# Output:
# Hello Alice!
# Hello Bob!
# Hello Charlie!

#5. Arbitrary positional Arguments
def greet(*args):
    for name in args:
        print(f"Hello {name}!")
print("**Arbitrary positional Arguments:")
greet("Alice", "Bob", "Charlie")
# Output:
# Hello Alice!
# Hello Bob!
# Hello Charlie!

#6. Arbitrary keyword Arguments
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
greet(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

