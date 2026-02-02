# Write a program that takes three numbers and prints the largest one using if-else.

def find_largest():
    try:
        a = int(input())
        b = int(input())
        c = int(input())
    except ValueError:
        return "Invalid input"
    if (a > b) and (a > b): 
        return "a is largest"
    elif (b > a) and (b > c):
        return "b is largest"
    else:
        return "c is largest"

def main():
    print(find_largest())

if __name__ == "__main__":
    main()
