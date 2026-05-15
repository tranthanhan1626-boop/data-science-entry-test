# Reverses a given string and returns the reversed result. First check if s is a string or not.

def string_reverse(s):
    if not isinstance(s, str):
        return -1

    return s[::-1]


print(string_reverse("Hello World"))
print(string_reverse("Python"))