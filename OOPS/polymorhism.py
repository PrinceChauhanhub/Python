class Animal:
    def speaks(self):
        pass
class Dog(Animal):
    def speaks(self):
        print("barks")
class Cat(Animal):
    def speaks(self):
        print("meow")
class Cow(Animal):
    def speaks(self):
        print("mooo")

dog=Dog()
cat=Cat()
cow=Cow()

dog.speaks()
cat.speaks()
cow.speaks()