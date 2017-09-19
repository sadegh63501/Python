class User :
    def __init__(self,name):
        self.name=name

    def printname(self):
        print("Name = ",self.name)

class Student(User):
    def __inti__(self,name):
        self.name=name
    def studentname(self):
        print("Student Name = ",self.name)


print("-------------------User Class")
me=User("Sadegh")
me.printname()

print("-------------------Inheritance Class")
you=Student("Hesam")
you.printname()
you.name="mohamad"
you.studentname()
        
