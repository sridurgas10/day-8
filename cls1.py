# Task 1:
#Create a `Car` class with attributes: brand, model, and year. Add a method to display car details.
class Car:
    def __init__(self,model,brand,year):
        self.model=model
        self.brand=brand
        self.year=year
    def cardetail(self):
       print(f"The car is a {self.year} {self.brand} {self.model}") 
       
car1=Car("creamy","toyoto",2022)
car1.cardetail()
