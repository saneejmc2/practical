def divisible_by_5():
    # Return a list of numbers divisible by 5
    return [i for i in range(1, 101) if i % 5 == 0]


def main():
    print(divisible_by_5())

if __name__ == "__main__":
    main()