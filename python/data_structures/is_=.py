# write a script understand 'is' and '==' 
# == checks for value equality (whether two objects have equivalent content), 
# # whereas is checks for identity (whether two references point to the exact same memory address).
a = 5
b = 5
c = [1, 2, 3]
d = [1, 2, 3]

print(f"a == b: {a == b}")  # True
print(f"a is b: {a is b}")  # True
print(f"ID of a: {id(a)}, ID of b: {id(b)}")  # Same memory address


print(f"c == d: {c == d}")  # True
print(f"c is d: {c is d}")  # False
print(f"ID of c: {id(c)}, ID of d: {id(d)}")  # Different memory addresses
