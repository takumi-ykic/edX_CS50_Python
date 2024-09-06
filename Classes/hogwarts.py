# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryfindor", "Gryfindor", "Gryfindor", "Slytherin"]

# students = {"Hermione": "Gryfindor", 
#             "Harry": "Gryfindor", 
#             "Ron": "Gryfindor",
#             "Draco": "Slytherin"}
# print(students)
# print(students["Hermione"])

# for student in students:
#     print(student, students[student], sep=", ")


# print(students)
# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])


students = [
    {"name": "Hermione", "house": "Gryfindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryfindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryfindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")