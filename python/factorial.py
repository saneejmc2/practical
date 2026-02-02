#Write a program to find the factorial of a number using while loop. Factorial of n = n × (n-1) × ... × 1.
# Hint: Initialize result=1, multiply while n > 0, decrement n each time

def factorial():
    try:
        n = int(input())
    except ValueError:
        return "Invalid Number"
    result = 1
    while n > 0:
        result = result * n
        n = n -1
    return result

def main():
    print(factorial())
if __name__ == "__main__":
    main()
