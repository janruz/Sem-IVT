def is_password_strong(password: str):
    any_upper = any_lower = any_numbers = False
    for character in password:
        any_upper = "A" <= character <= "Z" if not any_upper else any_upper
        any_lower = "a" <= character <= "z" if not any_lower else any_lower
        any_numbers = "0" <= character <= "9" if not any_numbers else any_numbers
    return len(password) >= 8 and any_upper and any_lower and any_numbers


user_interested = True
while user_interested:
    user_password = input("Enter a password to check: ")
    print("Congratulations! Your password is strong." if is_password_strong(user_password) else "Your password is weak. Try to think up a better one.")
    user_interested = False if input("Do you want to continue? [y/n] ") == "n" else True