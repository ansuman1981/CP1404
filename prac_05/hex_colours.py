"""
CP1404 Practical
Hexadecimal colour lookup
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Black": "#000000",
    "Blue": "#0000FF",
    "Brown": "#A52A2A",
    "Coral": "#FF7F50"
}

color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        print(color_name, "is", COLOUR_TO_HEX[color_name])
    except ValueError:
        print("Invalid color name")
    color_name = input("Enter color name: ").title()