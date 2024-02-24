class  Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def call_details(self):
        long_name= f"{self.year} {self.model} {self.make}"    
        return long_name

new_car=Car(1985,'a4',2021)
print(new_car.name)
print(new_car.call_details())