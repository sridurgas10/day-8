class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

       
    def area(self):
        #Area=Length*width
       # print(f"area of rectangle is {self.length}*{self.width}")
        return self.length*self.width

    def perimeter(self):
        return 2 *(self.length+self.width)
       
        #print(f"perimeter of the rectangle is {self.length}{self.width}")
        
rectangle=Rectangle(2,4) 
print("Area " ,rectangle.area())
print("Perimeter",(rectangle.perimeter())  )    