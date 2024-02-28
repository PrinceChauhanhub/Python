class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("role is:",self.role)
        print("dept is:",self.dept)
        print("salary is:",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT",200000)

eng=Engineer("pawan","25")
eng.showDetails()