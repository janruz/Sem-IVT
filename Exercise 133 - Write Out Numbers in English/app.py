from Cheque import Cheque

print("Welcome to console cheque maker!")

user_interested = True
while user_interested:

    try:
        payer_name = input("Enter payer's name: ")
        payee_name = input("Enter payee's name: ")
        money = int(input("Enter the amount of money: "))

        cheque = Cheque(payee_name, payee_name, money)
        print("You have just created the following cheque:")
        print(str(cheque))
    except Exception:
        print("Something went wrong! Try again.")
    
    user_interested = False if input("Do you want to make more cheques? [y/n]") == "n" else True