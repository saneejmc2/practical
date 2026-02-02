def tuple_demo():
    # Create tuple t1 = (1, 2, 3)
    # Create tuple t2 = (4, 5)
    # Concatenate to create t3 = t1 + t2
    # Return dict with original t1, t2, and combined t3
    t1 = (1, 2, 3)
    t2 = (4, 5)
    t3 = t1 + t2
    return {"t1":t1,"t2":t2,"t3":t3}    

def main():
    print(tuple_demo())

if __name__ == "__main__":
    main()