from guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2020, 500)

print("Gibson L-5 CES get_age() - Expected 100", guitar1.get_age())
print("Another Guitar get_age() - Expected 9. Got", guitar2.get_age())

print("Gibson L-5 CES is_vintage() - Expected True. Got", guitar1.is_vantage())
print("Another Guitar is_vintage() - Expected False. Got", guitar2.is_vantage())
