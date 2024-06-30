class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {new_owner}")

# Create a few instances of Vehicle
vehicle1 = Vehicle("123ABC", "Car", "Alice")
vehicle2 = Vehicle("456DEF", "Motorcycle", "Bob")
vehicle3 = Vehicle("789GHI", "Truck", "Charlie")

# Demonstrate changing the owner
print(f"Original owner of vehicle1: {vehicle1.owner}")
vehicle1.update_owner("David")
print(f"New owner of vehicle1: {vehicle1.owner}")

print(f"Original owner of vehicle2: {vehicle2.owner}")
vehicle2.update_owner("Eve")
print(f"New owner of vehicle2: {vehicle2.owner}")

print(f"Original owner of vehicle3: {vehicle3.owner}")
vehicle3.update_owner("Frank")
print(f"New owner of vehicle3: {vehicle3.owner}")
