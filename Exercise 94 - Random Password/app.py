from random import randint

safety_levels = ["WEAK", "OK", "SAFE", "SUPER-SAFE"]
default_safety_level = safety_levels[-1]


def generate_password(safety_level=default_safety_level):
    lengths = get_min_max_lenghts_for(safety_level)
    length = randint(lengths[0], lengths[1])
    password = ""
    for i in range(length):
        password += chr(randint(33, 126))
    return password


def get_min_max_lenghts_for(safety_level):
    base = safety_levels.index(safety_level) + 1
    return base * 7, base * 10


def get_safety_level():
    answer = input("How safe do you want your password to be? " + str(safety_levels).replace(',', ' /').replace('\'', ''))
    for level in safety_levels:
        if level == answer.upper():
            return level
    else:
        return default_safety_level


user_interested = True
while user_interested:
    print("Your new password is:")
    password = generate_password(safety_level=get_safety_level())
    print(password)
    user_interested = False if input("Do you need more? [y/n]") == "n" else True
