from taxi import Taxi

my_taxi = Taxi("prius1", 100, 1.23)
print(my_taxi)
my_taxi.drive(40)
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")
my_taxi.get_fare()
my