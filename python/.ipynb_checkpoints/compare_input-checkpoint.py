#Write a program that takes a number as input and prints whether it is positive, negative, or zero.


def compare_input():
    # Write a program that takes a number as input and prints whether it is positive, negative, or zero.
    try:
        num = int(input())
    except ValueError:
        return "Invalid input"
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    print(compare_input())

if __name__ == "__main__":
    main()
