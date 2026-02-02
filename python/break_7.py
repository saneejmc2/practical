#Print numbers from 1 to 10, but stop (break) when number equals 7. Do not print 7.
#Hint: Use if num == 7: break before printing, write in single function in least lines of code.
def break_at_7():
    result = []
    for i in range(1, 11):
        if i == 7:
            break
        result.append(i)
    return result
def main():
    print(break_at_7())
if __name__ == "__main__":
    main()

