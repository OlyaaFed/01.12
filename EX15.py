def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def add_fractions(a, b, c, d):
    common_denominator = lcm(b, d)
    numerator_sum = a * (common_denominator // b) + c * (common_denominator // d)
    common_divisor = gcd(numerator_sum, common_denominator)
    result_numerator = numerator_sum // common_divisor
    result_denominator = common_denominator // common_divisor
    return result_numerator, result_denominator

a = int(input("числитель первой  (a): "))
b = int(input("знаменатель первой  (b): "))
c = int(input("числитель второй  (c): "))
d = int(input("знаменатель второй  (d): "))
result_numerator, result_denominator = add_fractions(a, b, c, d)
print(f"Сумма: {result_numerator}/{result_denominator}")