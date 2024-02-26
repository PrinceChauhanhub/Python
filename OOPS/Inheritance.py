class Car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.odometer_reding=0
        
    def get_descriptive(self):
        long_name=f"{self.name} {self.model} {self.year}"
        return long_name

class ElectricCar(Car):
    def __inti__(self,name,model,year):
        super().__init(name,model,year)


my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive())