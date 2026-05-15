# Finds the first negative number in a list using a while loop.
# while loop begins with i=0 < len(lst)=6 => lst(O)=3 > 0 -> i+=1 continue to the one lst[2]= -1 -> return -1 end code.

def find_first_negative(lst):
    i = 0

    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1

    return "No negatives"


print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))