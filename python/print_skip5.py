# Print numbers from 1 to 10, but skip multiples of 5 using continue statement.
def print_skip5():
    for i in range(1, 11):
        if i % 5 == 0:
            continue
        print(i)    
def main():
    print_skip5()   
if __name__ == "__main__":
    main()
        