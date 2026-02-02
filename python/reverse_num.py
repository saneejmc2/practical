# Write a program to reverse a number using while loop. Example: 123 becomes 321.
def reverse_num():
    try:
        num = int(input())
    except ValueError:
        return "Invalid Number"
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    return reverse

def main():
    print(reverse_num())
if __name__ == "__main__":
    main()