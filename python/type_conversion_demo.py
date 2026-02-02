def type_conversion_demo(num):
    # Start with num (int)
    # Convert to float
    # Convert to string
    # Return dict with each stage: original, as_float, as_string    
    # Expected: {"as_float":{"type":"float","value":42},"original":{"type":"int","value":42},"as_string":{"type":"str","value":"42.0"}}

    return {"as_float":{"type":typeFloar[8:13],"value":toFloat},"original":{"type":typeInt[8:11],"value":integer},"as_string":{"type":typeString[8:11],"value":toString}}
 

def main():
    print(type_conversion_demo(42))

if __name__ == "__main__":
    main()