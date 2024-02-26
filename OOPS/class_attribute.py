class Person:
    name="anonumous"
    
    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("prince")
print(p1.name)
print(Person.name)