#Write a function that reverses digits of a number using a stack. Example: 12345 → 54321
#Hint: Push each digit to stack, then pop to build reversed number.
import json

def reverse_number(num):
    sign = 1
    if num < 0:
        sign = -1
        num = -num
    stack = []
    # Push each digit
    for digit in str(num):
        stack.append(digit)
    # Pop and build result
    result = ""
    while stack:
        result += stack.pop()
    return sign * int(result)
# Test your implementation
result1 = reverse_number(12345)
result2 = reverse_number(9876)
result3 = reverse_number(-12345)
output = {
    "result1": result1,
    "result2": result2,
    "result3": result3
}
print(json.dumps(output))
