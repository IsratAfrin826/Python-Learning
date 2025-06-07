class Student:
    roll = " "
    gpa = ""


    def __init__(self, roll ,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll},GPA : {self.gpa}")


israt = Student(101,3.90)
israt.display()


asma = Student(102,3.95)
asma.display()