class Student:
    def __init__(self,name,age,student_no,course):
        self.name=name
        self.age=age
        self.student_no=student_no
        self.course=course

    def study(self,unit):
        print(f"{self.name}studies {unit}")

    def eat(self,food):
        print(f"{self.name}eats{food}")

    def sleep(self,time):
        print(f"{self.name}sleeps{time}")

    def display_info(self):
        print(f"Name:{self.name} ,S.NO:{self.student_no} ,Age:{self.age} ,Course.{self.course}")
        print('___User_Details___')
        print('______________________________________')




Student1=Student("Jack",20,"s001","Computer")
print(type(Student1))
print(Student1)
Student1.display_info()
Student1.study("002")
Student1.eat("rice")
Student1.sleep("12.00pm")

Student2=Student("Jane",20,"s002","DataScience")
print(type(Student2))
print(Student2)
Student2.display_info()
Student2.study("001")
Student2.eat("cake")
Student2.sleep("1.00am")





    
        
    