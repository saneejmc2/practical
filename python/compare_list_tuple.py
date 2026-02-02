import sys

def compare_list_tuple():
    # Create list and tuple with same elements: 1, 2, 3, 4, 5
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (1, 2, 3, 4, 5)
    # Get sizes using sys.getsizeof()
    # Return dict with list_size, tuple_size, and smaller ("list" or "tuple")
    list_size = sys.getsizeof(my_list)
    tuple_size = sys.getsizeof(my_tuple)
    return {"smaller": "list" if list_size < tuple_size else "tuple"}

def main():
    print(compare_list_tuple())

if __name__ == "__main__":
    main()