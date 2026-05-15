def find_and_replace(lst, find_val, replace_val):
    #lst is the list you want to search, find_val: value you want to find, replace_val: value you want to replace
    if not isinstance(lst, list):
        return -1
# if lst is not a list => -1 end code
# lst is a list => i in range based on lenght of lst if the value in list = find_val => replace it by replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


# Task 2
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))