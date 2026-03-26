from unreliable_car import UnreliableCar

# Make two cars with different reliability
reliable_car = UnreliableCar("Mostly Reliable", 100, 90)  # 90% reliable
unreliable_car = UnreliableCar("Barely Goes", 100, 30)  # 30% reliable

print(reliable_car)
print(unreliable_car)