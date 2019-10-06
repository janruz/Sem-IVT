def take_decimal_input(input_message):
    while True:
        try:
            return float(input(input_message))
        except ValueError:
            print("Wrong input format!")

FEET_IN_ACRE = 43560
width = take_decimal_input("Enter width of your field in feets: ")
length = take_decimal_input("Enter length of your field in feets: ")
area = width * length # in feet
print(f"The area of your field is {round(area / FEET_IN_ACRE, 2)}")# in acres