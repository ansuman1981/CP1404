from guitar import Guitar

guitars = []

name = input("name:")
while name != '':
    year = int(input("year:"))
    cost = float(input("cost:"))
    guitar = Guitar(name,year,cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("name:")
    print("These are my guitars:")

for i, guitar in enumerate(guitars, 1):
    if guitar.is_vantage():
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>10} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

