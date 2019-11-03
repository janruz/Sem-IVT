def add_left_padding_to(string_value: str, max_string_len):
    padding = " " * ((max_string_len + 1) - len(string_value))
    return padding + string_value


def print_top_row():
    print(" " * (max_string_len+1), end="")
    
    for item_in_row in range(1, max + 1):
        print(add_left_padding_to(str(item_in_row), max_string_len), end="")

    print("")


def print_row(row_number):
    print(add_left_padding_to(str(row_number), max_string_len), end="")

    for item_in_row in range(1, max + 1):
        print(add_left_padding_to(str(row_number * item_in_row), max_string_len), end = "")

    print("")


def print_table():
    print_top_row()
    for row_number in range(1, max + 1):
        print_row(row_number)


def input_number(msg: str):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Try again.")


user_interested = True
while user_interested:
    max = input_number("Enter the max number for the multiplication table: ")
    max_string_len = len(str(max ** 2))
    print_table()

    user_interested = False if input("Do you want to continue? [y/n]") == "n" else True