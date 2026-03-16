from guitar import Guitar
import csv

def main():
    guitars = []
    load_guitars(guitars)
    #display all guitars
    display_guitars(guitars)
    new_guitars(guitars)
    guitars.sort()
    # Display final sorted list
    save_guitars(guitars)


def save_guitars(guitars):
    print("\nThese are my guitars:")
    display_guitars(guitars)

    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        out_file.write(f"{guitar.Name}, {guitar.Year},{guitar.Cost}\n")
    out_file.close()
    print("\nGuitars have been saved to guitars.csv")


def new_guitars(guitars):
    print("\nEnter your new guitars (leave name blank to stop):")
    Name = input("enter name")
    while Name != "":
        Year = int(input("enter year"))
        Cost = float(input("enter cost"))
        guitars.append(Guitar(Name, Year, Cost))
        print(f"{Name} added.\n")
        Name = input("enter name")


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def load_guitars(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    guitars.sort()


main()