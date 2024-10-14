class UniversityMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(UniversityMember):
    def __init__(self, name, age, department_name):
      
        self.name = name
        self.age = age
        self.department_name = department_name

    def display_info(self):
       
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Department: {self.department_name}")

class Staff(UniversityMember):
    def __init__(self, name, age, position):
       
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Position: {self.position}")

teacher = Teacher("Utsav", 19, "Electrical")
teacher.display_info()

staff = Staff("Ram", 19, "Manager")
staff.display_info()

member = UniversityMember("Bijaya", 19)
member.display_info()
