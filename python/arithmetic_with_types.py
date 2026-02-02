def arithmetic_with_types(a, b):
    # Perform operations and return dict with results and types
    # Keys: add, sub, mul, div, floor_div, mod
    # Each should have "value" and "type" as string
    add = a + b
    return {"add":{"type":type(add).__name__,"value":add},"div":{"type":type(div).__name__,"value":div},"mod":{"type":type(mod).__name__,"value":mod},"mul":{"type":type(mul).__name__,"value":mul},"sub":{"type":type(sub).__name__,"value":sub},"floor_div":{"type":type(floor_div).__name__,"value":floor_div}}
    
def main():
    print(arithmetic_with_types(10, 3))

if __name__ == "__main__":
    main()