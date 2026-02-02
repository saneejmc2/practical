#Write a  program to Calculate electricity bill based on units consumed:\n0-100 units: Rs 5 per unit\n101-200 units: Rs 7 per unit\n201-300 units: Rs 10 per unit\nAbove 300: Rs 15 per unit\nPrint the total bill amount.
def ebill_calc():
    try:
        units = int(input())
    except ValueError:
        return "Invalid units"
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    elif units <= 300:
        return 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        return 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15
    
def main():
    print(ebill_calc())
if __name__ == "__main__":
    main()