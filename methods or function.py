class student:
    roll = " "
    gpa = ""


    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll},GPA : {self.gpa}")


Israt = student()
Israt.set_value(101,3.90)
Israt.display()


Asma = student()
Asma.set_value(102,3.95)
Asma.display()