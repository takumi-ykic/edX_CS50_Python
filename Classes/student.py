import sys

class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "House"
            case "Otter":
                return "Sea animal"
            case "Jack Russell terrier":
                return "Dog"
            
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name    
    
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        
        return cls(name, house, patronus)

def main():
    # name = input("Name: ")
    # house = input("House: ")
    # name, house = get_student()
    # student = get_student()
    student = Student.get()

    if student.name == "Padma":
        student.house = "Ravenclaw"

    # print(f"{name} from {house}")
    # print(f"{student['name']} from {student['house']}")
    # print(f"{student.name} from {student.house}")
    print(student)
    print("Expecto Patronum!")
    print(student.charm())

# def get_name():
#     name = input("Name: ")
#     return name

# def get_house():
#     return input("House: ")

# def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # return (name, house)

    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student

    # name = input("Name: ")
    # house = input("House: ")
    # return {"name":name, "house":house}

    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")

    # name = input("Name: ")
    # house = input("House: ")
    # patronus = input("Patronus: ")
    # return Student(name, house, patronus)

if __name__ == "__main__":
    main()
