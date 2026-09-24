s='Hello World'
iter_s = iter(s)
print(next(iter_s))  # Output: H
print(next(iter_s))  # Output: e    
print(next(iter_s))  # Output: l

num = [1]
iter_num = iter(num)
print(next(iter_num))  # Output: 1
print(next(iter_num))  # Raises StopIteration