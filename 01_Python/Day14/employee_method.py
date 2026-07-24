class Employee:
    def __init__(self,name,roll,salary):
        self.name=name
        self.roll=roll
        self.salary=salary
    def display_info(self):
        print("Employee Name:",self.name)
        print("Employeee roll:",self.roll)
        print("Salary:",self.salary)
    def work(self):
        print(self.name ,"work as " ,self.roll)
emply=Employee("Athira","Software Developer",30000)
emply.display_info()
emply.work()
    