def demonstrate_primitives():
    # Create variables for each primitive type
    int_var = 10
    float_var = 3.14
    bool_var = "true"
    str_var = "Hello"
    
    # Print value and type for each
    #print(f"Value: {int_var}, Type: {type(int_var)}")
    #print(f"Value: {int_var}, Type: {type(int_var)}")
    
    # Return a dictionary with all values
    return {"int_val": int_var,"str_val":str_var, "bool_val": bool(bool_var), "float_val":float_var }

def main():
    print(demonstrate_primitives())

if __name__ == "__main__":
    main()