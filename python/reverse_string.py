def reverse_string(s):
    # Return reversed string without using built-in reverse functions or slicing.
    #    return s[::-1]
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string

def main():
    print(reverse_string("Hello World"))

if __name__ == "__main__":
    main()
