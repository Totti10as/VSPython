

# course = "Python"
# temp = 20
# # print(len(course))
# print(course.upper())

# x = input("x: ")
# print(type(x))

# if temp > 20:
#     print("print")
#     print("do not print")
# print("Done")


# for number in range(3):
#     print("Attempt", number+1, (5) * ".")

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We've {count} even numbers")

# Print Function
def welocme(Fname, Sname):
    print(f"Hi {Fname} {Sname}")
    print("Welcome on board")


welocme("Stas", "Masarsky")
welocme("Suzuki", "Vitara")


# Return Function
def get_welcome(name):
    return f"Hi {name}"


# open a file and write into it
message = get_welcome("Toyota")
file = open("content.txt", "w")
file.write(message)
