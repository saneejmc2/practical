def demonstrate_non_primitives():
    # Create examples of each:
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_set = {1, 2, 3}
    my_dict = {"a": 1, "b": 2}
    
    # Return dict with type names and lengths
    return {"set":{"type": str(type(my_set))[8:11],"length":len(my_set)},"dict":{"type":str(type(my_dict))[8:12],"length": len(my_dict)},"list":{"type":str(type(my_list))[8:12],"length":len(my_list)},"tuple":{"type":str(type(my_tuple))[8:13],"length":len(my_tuple)}}
    
def main():
    print(demonstrate_non_primitives())

if __name__ == "__main__":
    main()