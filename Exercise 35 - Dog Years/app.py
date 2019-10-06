def take_decimal_input(input_msg, error_msg):
    while True:
        try:
            return float(input(input_msg))
        except ValueError:
            print(error_msg)

def human_years_to_dog_years(human_years):
    convert_ratio_for_first_two_years = 10.5
    convert_ratio_for_other_years = 4
    if human_years >= 2:
        return (2 * convert_ratio_for_first_two_years) + ((human_years - 2) * convert_ratio_for_other_years)
    else:
        return human_years * convert_ratio_for_first_two_years

user_interested = True
while user_interested:
    print("*" * 25)
    human_years = take_decimal_input("Enter the number of human years to convert: ", "Wrong value! Please try again.")
    dog_years = human_years_to_dog_years(human_years)
    print(f"{human_years} in human years is {dog_years} in dog years.")
    user_interested = False if input("Do you want to keep converting to dog years? [y/n]") == "n" else True