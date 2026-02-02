# Input: A positive integer n\nn = int(input())\n\n# Your code here\n

def print_num():
    try:
        n = int(input())
    except ValueError:
        return "Invalid Number"

    for i in range(1,n+1):
        print(i)    

def main():
    print(print_num())
if __name__ == "__main__":
    main()
