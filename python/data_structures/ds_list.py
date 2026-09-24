empty = []
print(empty)

letters = ['a', 'b', 'c', 'd']
print(letters)

print(type(letters))

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

mixed = [1, 'a', 2, 'b']
print(mixed)

list_letters = list( 'Python' )
print(list_letters)

list_numbers = list( range( 1, 11 ) )
print(list_numbers)

list_numbers = list( range( 1, 11, 2 ) )
print(list_numbers)

list_numbers = list( range( 10, 0, -1 ) )
print(list_numbers)

list_numbers = list( range( 10, 0, -2 ) )
print(list_numbers)

matrix = [[1, 2, 3, 4], 
         ['a', 'b', 'c', 'd'],
         ['!', '@', '#', '$']]
print(matrix)


print('Reading matrix using for loop')
index = 0
while index < len(matrix):
    inner_index = 0
    while inner_index < len(matrix[index]):
        print(f"Row {index}, Column {inner_index}: {matrix[index][inner_index]}")
        inner_index += 1
    print(f"Outer Row {index}: {matrix[index]}")
    index += 1

print('Slicing lists/matrix')
letters = ['a', 'b', 'c', 'd']
print(letters[1:3])
print(matrix[2][1:3])

print('\nUnpacking lists:')
personal_data = ['John', 'Doe', 30, 'New York']
first_name, last_name, age, city = personal_data
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"City: {city}")

first_name, last_name, *other_data = personal_data
print(f"Name: {first_name} {last_name}")    
print(f"Other Data: {other_data}")


print('\nSkipping list elements by not saving them:')
_, last_name, *_ = personal_data
print(f"Last Name: {last_name}")