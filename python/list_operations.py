def list_operations():
    # Create initial list [1, 2, 3]
    # Add 4 and 5 using append or extend
    # Remove element 2 using remove
    # Return the final list
    # Expected: [1, 3, 4, 5]
    initial_list = [1, 2, 3]
    initial_list.extend([4, 5])
    initial_list.remove(2)
    return initial_list

def main():
    print(list_operations())

if __name__ == "__main__":
    main()