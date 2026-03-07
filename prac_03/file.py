#1
name = input("enter your name:")
file =open("name.txt", "w")
file.write(name)
file.close()

#2

file = open("name.txt" , 'r')
name = file.read()
file.close()
print(f"Hi {name}!")

#3
with open("number.txt", "r") as file:
    first = int(file.readline())
    second = int(file.readline())

total = first + second
print(total)


#4
total = 0
with open("number.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)