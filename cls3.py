class Person:

   def __init__(self,position,salary):
    self.position=position
    self.salary=salary



class Employee(Person):
    def dis_info(self):
       print(f"the employee position is {self.position} and his salary is {self.salary}")
employee1=Employee("teacher",25000)
               
employee1.dis_info()
