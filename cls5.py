class Shoppingcart:
    def __init__(self,proname,quantity,price):
        self.proname=proname
        self.quantity=quantity
        self.price=price
    def additem(self):
        return f"proname:{self.proname} quantity:{self.quantity} price{self.price}  "
    def remitem(self):


cart=Shoppingcart("mobile",1,10000)
print("added cart items:"cart.additem())
for cart in Shoppingcart:
    print(cart)      