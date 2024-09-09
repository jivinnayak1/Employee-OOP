class Employee:
    def __init__(self,Name,ID,Salary=90000):
        self.Name = Name
        self.ID = ID
        self.Salary = Salary

    def Wish(self):
        print(f"Happy Birthday {self.Name}")

    def Terminate(self):
        print(self.Name+" You are fired. No need to come tommorow")

    def Promotion(self):
        print(self.Name+" Congratulations, you are promoted")

emp1 = Employee("Jivin",1234)
emp2 = Employee("Adib",5678)
emp3 = Employee("Jay",5678)
emp4 = Employee("Vir",5678)
    
print(emp1.Wish())
print(emp2.Terminate())
print(emp3.Promotion())
print(emp4.Wish())