"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""



def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_month = int(input("How many months? "))
    for month in range(1, number_of_month + 1):
        income = float(input(f"enter the income for month {month}: "))
        incomes.append(income)
    display_income(incomes, number_of_month)


def display_income(incomes, number_of_month):
    """Print income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        print(f"month {month} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
