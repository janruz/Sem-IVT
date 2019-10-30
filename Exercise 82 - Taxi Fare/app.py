BASE_FARE = 4.00 # $
DISTANCE = 140 # m
FARE_PER_DISTANCE = 0.25 # $


def calculate_taxi_fare(distance):
    return round(BASE_FARE + (distance / DISTANCE) * FARE_PER_DISTANCE, 2)


def take_distance():
    while True:
        try:
            return float(input("Enter the distance travelled: "))
        except ValueError:
            print("Try again.")


user_interested = True
while user_interested:
    print("Welcome to Taxi Fare Calculator!")
    print(calculate_taxi_fare(take_distance()))

    user_interested = False if input("Wanna continue? [y/n]") == "n" else True    