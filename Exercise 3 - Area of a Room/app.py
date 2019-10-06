def take_decimal_input(input_message):
    while True:
        try:
            return float(input(input_message))
        except ValueError:
            print("Wrong input format!")        

width = take_decimal_input("Enter the width of your room in meters: ")
length = take_decimal_input("Enter the length of your room in meters: ")
print(f"The area of your room is {width * length}")