def take_decimal_input(input_msg, error_msg):
    while True:
        try:
            return float(input(input_msg))
        except ValueError:
            print(error_msg)

def calculate_single_root(a, b, c, discriminant, multiplier):
    return (-b + multiplier * (discriminant ** (1 / 2))) / (2 * a)

def calculate_discriminant(a, b, c):
    return (b ** 2 - 4 * a * c)

def calculate_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    roots = []
    if discriminant >= 0:
        roots.append(calculate_single_root(a, b, c, discriminant, 1))
        if discriminant > 0:
            roots.append(calculate_single_root(a, b, c, discriminant, -1))
    return roots

user_interested = True
while user_interested:
    a = take_decimal_input("Enter a: ", "Not a number! Try again")
    b = take_decimal_input("Enter b: ", "Not a number! Try again")
    c = take_decimal_input("Enter c: ", "Not a number! Try again")

    roots = calculate_roots(a, b, c)
    print(f"The function has {len(roots)}: {roots}")

    user_interested = False if input("Do you want to calculate more roots? [y/n]") == "n" else True