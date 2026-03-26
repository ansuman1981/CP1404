from unreliable_car import UnreliableCar

# Make a car with 30% reliability
unreliable_car = UnreliableCar("Barely Goes", 100, 30)

total_distance = 0
attempts = 100

for i in range(attempts):
    distance = unreliable_car.drive(1)
    total_distance += distance

print(f"Total distance driven in {attempts} attempts: {total_distance}")