class Student:
    def __init__(self,marks):
        #self.name=name
        self._marks=marks

    def getmarks(self):
        return self._marks
student1=Student(460)
print("the student1 mark is ",student1.getmarks()  )  