#Write a program to count the number of vowels (a, e, i, o, u) in a given string (case-insensitive).
# Hint: Convert to lowercase and check if each character is in "aeiou"
def count_vowels():
    try:
        text = input()
    except ValueError:
        return "Invalid String"
    count = 0
    for i in text.lower():
        if i in "aeiou":
            count += 1
    return count

def main():
    print(count_vowels())
if __name__ == "__main__":
    main()
