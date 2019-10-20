notes_faces = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin" }

def input_denomination():
    denomination = int(input("Enter any dollar denomination: "))
    if not is_denomination_valid(denomination):
        raise ValueError()
    return denomination

def is_denomination_valid(denomination):
    return denomination in notes_faces.keys()

user_interested = True
while(user_interested):
    denomination = 0

    while not is_denomination_valid(denomination):
        try:
            denomination = input_denomination()
        except ValueError:
            print("No such note exists! Enter an existing denomination.")
    
    print(f"There is {notes_faces[denomination]} on ${denomination} banknote.")
    user_interested = False if input("Do you want to continue? [y/n]") == "n" else True