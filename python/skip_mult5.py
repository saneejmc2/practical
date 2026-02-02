#def skip_mult5():
#    # Return a list of numbers divisible by 5
#    return [i for i in range(1, 11) if i % 5 != 0]
## how to to do using if not divisible by 5
#
#
#def main():
#    print(skip_mult5())
#
#if __name__ == "__main__":
#    main()

#Print numbers from 1 to 10, but skip multiples of 5 using continue statement.

#10 pts
#💡 Hint: Use if num % 5 == 0: continue inside the loop

def skip_mult5():
    result = []
    for i in range(1, 11):
        if i % 5 == 0:
            continue
        result.append(i)
    return result

def main():
    print(skip_mult5())
if __name__ == "__main__":
    main()  
