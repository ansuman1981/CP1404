# display all the odd numbers between 1 and 20 with a space between each one
"""
for i in range(1,21,2):
    print(i, end=" ")
print()

#a
for count in range(0,101,10): # 0-100
    print(count, end=" ")

#b
for count_down in range(20,0,-1): #20-1
    print(count_down, end=" ")
"""
#c
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*",end ="")

#d
number_of_lines = int(input("Number of lines: "))
for line_number in range(1, number_of_lines+1):
    print("*" * line_number)


