# Write a program to find the sum of first n natural numbers using a for loop.
def sum_num():
    try:
        n = int(input())
    except ValueError:
        return "Invalid Number"
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def main():
    print(sum_num())
if __name__ == "__main__":
    main()