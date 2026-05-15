def update_dictionary(dct, key, value):
    # Updates a dictionary by adding a new key-value pair or replacing an existing value.
    if key in dct:
        print(dct[key])

    dct[key] = value
    return dct


# Task 2
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))