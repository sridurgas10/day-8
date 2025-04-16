### Task 8:
#Use inheritance to model `Shape` class and subclasses `Circle` and `Square`.
class Shape:
    def draw(self):
        print("the shape")
class Circle(Shape):
    def draw(self):  
        print("the shape is circle")
class Square(Shape):
    def draw(self):    
        print("the shape is square")
circle=Circle()
circle.draw()
square=Square()
square.draw()
