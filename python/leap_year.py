#Write a program to check whether a given year is a leap year or not. A leap year is divisible by 4, but not by 100 unless also divisible by 400.
def leap_year():
    try:
        year = int(input())
    except ValueError:
        return "Invalid year"
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"
    
def main():
    print(leap_year())
if __name__ == "__main__":
    main()