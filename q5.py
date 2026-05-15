# Checks if one numeric value is divisible by another.

def check_divisibility(num, divisor):
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False

    if divisor == 0:
        return False

    return num % divisor == 0


print(check_divisibility(10, 2))
print(check_divisibility(7, 3))