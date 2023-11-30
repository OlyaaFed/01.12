def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def add_fractions(A, B, C, D):
    common_denominator = lcm(B, D)
    numerator_sum = A * (common_denominator // B) - C * (common_denominator // D)
    common_divisor = gcd(numerator_sum, common_denominator)
    result_numerator = numerator_sum // common_divisor
    result_denominator = common_denominator // common_divisor
    return result_numerator, result_denominator

A = int(input("числитель первой (A): "))
B = int(input("знаменатель первой (B): "))
C = int(input("числитель второй (C): "))
D = int(input("знаменатель второй (D): "))
result_numerator, result_denominator = add_fractions(A, B, C, D)
print(f"Разность : {result_numerator}/{result_denominator}")