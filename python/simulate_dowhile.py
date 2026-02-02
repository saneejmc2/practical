#Python does not have a do-while loop. Simulate one using while True + break.\n\nWrite a program that keeps asking for a password until the user enters "python123". Print "Access Granted" when correct password is entered.
#Hint: Use while True, check password, break if correct, else print "Try again"
# Test with both correct(python123) and incorrect(wrong\npython123) passwords.
def simulate_dowhile():
    while True:
        entered = str(input())
        if entered == "python123":
            print("Access Granted")
            break
        else:
            print("Try again")  
def main():
    print(simulate_dowhile())
if __name__ == "__main__":
    main()
