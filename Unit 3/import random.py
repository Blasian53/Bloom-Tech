import random


class Student:
    def __init__(self, name, age) -> None:
        self.age = age
        self.name = name
    
    def grade(self, a):
        self.a = a
    
    def id(self, a):
        self.a = a

class BloomTechStudent(Student):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

def StudentGenerator():
    names = ['Bill', 'Fred', 'Steve', 'Alex']
    students = []
    for i in range(30):
        rand_names = random.choice(names)
        rand_age = random.randint(18,99)

        students.append(Student(rand_names,rand_age))
        students.append(BloomTechStudent(rand_names,rand_age))
    return students
 
print(StudentGenerator())