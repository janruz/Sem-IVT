def input_int(msg: str):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Try again")


def get_divisors_of(number: int):
    result = []
    for potential_divisor in range(1, number):
        if number % potential_divisor == 0:
            result.append(potential_divisor)
    return result


def is_perfect(number: int):
    all_divisors = get_divisors_of(number)
    total = 0

    for divisor in all_divisors:
        total += divisor

    return total == number


user_interested = True
while user_interested:
    top = input_int("Enter a limit for the numbers to test: ")
    for i in range(1, top + 1):
        print(f"{i} {'is perfect' if is_perfect(i) else 'is not perfect'}")
    user_interested = False if input("Do you want to continue? [y/n]") == 'n' else True