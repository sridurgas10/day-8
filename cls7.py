#Task 6:
#Create a `BankAccount` class that has deposit and withdraw methods with balance check.
class Student:
    def __init__(self,marks):
        
        self._marks=marks

    def getmarks(self):
        return self._marks
student1=Student(460)
print("the student1 mark is ",student1.getmarks()  )  
