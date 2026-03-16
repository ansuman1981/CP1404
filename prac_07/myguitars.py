from guitar import Guitar
import csv

def main():
    guitars = []
    in_file = open('guitars.csv','r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    #display all guitars
    for guitar in guitars:
        print(guitar)

main()