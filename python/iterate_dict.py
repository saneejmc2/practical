def iterate_dict():
    # Create dict: {"Alice": 85, "Bob": 92, "Charlie": 78}
    # Iterate and create list of "Name: Score" strings
    # Return the list
    my_dict = {"Alice": 85, "Bob": 92, "Charlie": 78}
    my_list = []
    for key, value in my_dict.items():
        my_list.append(f"{key}: {value}")
    return my_list

def main():
    print(iterate_dict())

if __name__ == "__main__":
    main()