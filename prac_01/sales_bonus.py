"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        print("Your sales are under $1,000.you get a 10% bonus.")
        total_bonus = sales *0.1
        print("Your total bonus:", total_bonus)
    if sales >= 1000:
        print("Your sales are under $1,000.you get a 15% bonus.")
        total_bonus = sales *0.15
        print("Your total bonus:", total_bonus)
    sales = float(input("Enter sales: $"))
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        print("Your sales are $1,000 or over. You get a 15% bonus.")
        total_bonus = sales *0.15
        print("Your total bonus:", total_bonus)
    else:
        print("Your sales are under $1,000. You get a 10% bonus.")
        total_bonus = sales *0.1
        print("Your total bonus:", total_bonus)
    sales = float(input("Enter sales: $"))