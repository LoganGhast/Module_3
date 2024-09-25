class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def create_automobile():
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car (e.g., Toyota): ")
    model = input("Enter the model of the car (e.g., Corolla): ")

    while True:
        try:
            doors = int(input("Enter the number of doors (2 or 4): "))
            if doors in [2, 4]:
                break
            else:
                print("Please enter either 2 or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number (2 or 4).")

    roof = input("Enter the type of roof (solid or sun roof): ").lower()

    car = Automobile(year, make, model, doors, roof)

    print("\nHere are the details of the car you entered:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")


create_automobile()
