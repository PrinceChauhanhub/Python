class Rectangle:
    def set_dimensions(self,width,height):
        self.width=width
        self.height=height
        
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2*(self.height+self.width)
        
        
#creating object
rect=Rectangle()
rect.set_dimensions(10,20)
print("the height and width are ",rect.height,"and ",rect.width)

print("The area is:",rect.area())
print("The perimeter is :",rect.perimeter()) 