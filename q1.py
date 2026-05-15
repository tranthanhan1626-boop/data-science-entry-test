def swap(x, y):
    # Defining function: if x or y not numeric -> -1; if numeric -> swap x,y=y,x
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    x, y = y, x
    print(x, y)


print(swap("Apple", 10))
swap(9, 17)