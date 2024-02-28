class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price>ord2.price
    
ord1=Order("kurkure",5)
ord2=Order("tedh emedhe",15)
print(ord1>ord2)
