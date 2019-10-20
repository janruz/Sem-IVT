def formula(degrees_celsius):
    return round((degrees_celsius * (9/5)) + 32, 1)

def print_in_columns(row_values, column_width):
    print("".join(str(value).ljust(column_width) for value in row_values))

def input_number(input_msg, error_msg):
    while True:
        try:
            return int(input(input_msg))
        except ValueError:
            print(error_msg)

def create_conversion_table(start, end, step):
    table = [(i, formula(i)) for i in range(start, end+step, step)]
    table.insert(0, ["Celsius", "Fahrenheit"])
    return table

def print_conversion_table(table):
    padding = 2
    column_width = max(len(str(value)) for row in table for value in row) + padding
    print("Temperature Conversion Table")
    print("*" * 30)

    for row in table:
        print_in_columns(row, column_width)

user_interested = True
error_msg = "Wrong input! Try again."
print("Welcome to PyTemperatureConverter")
while user_interested:
    start = input_number("Enter the start (in Celsius): ", error_msg)
    end = input_number("Enter the end (in Celsius): ", error_msg)
    step = input_number("Enter the step (in Celsius): ", error_msg)
    print_conversion_table(create_conversion_table(start, end, step))

    user_interested = False if input("Do you want to continue? [y/n]") == "n" else True