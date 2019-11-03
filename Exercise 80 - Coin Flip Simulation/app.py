from FlipSimulator import FlipSimulator
from Coin import Coin


def get_average(list):
    return sum(list) / len(list)


def output_simulation_outcomes():
    counter = 0

    for outcome in simulator.seek_consecutive_flips(3):
        print(outcome, end = " ")
        counter += 1
    
    print(f"({str(counter)} flips)")
    return counter


def run_simulation_series(n): # n times
    flips_needed = []

    for i in range(0, n):

        flips_needed.append(output_simulation_outcomes())

    return flips_needed


def ask_user_for_number_of_simulations():
    while True:
        try:
            return int(input("Enter the number of flip simulations: "))
        except ValueError:
            print("Try again.")


simulator = FlipSimulator(Coin())

print("*** Welcome to Coin Flip Simulator ***")
user_interested = True

while user_interested:
    
    flips_needed = run_simulation_series(ask_user_for_number_of_simulations())

    print(f"On average, {get_average(flips_needed)} flips were needed.")

    user_interested = False if input("Do you want to continue simulating? [y/n]") == "n" else True

print("*** Hope you enjoyed it. ***")