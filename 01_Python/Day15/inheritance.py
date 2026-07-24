class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("Employee Name:",self.name)
        print("Age:",self.age)
class employee(person):
    def __init__(self, name, age,role):
        super().__init__(name, age)
        self.role=role
    def display_emply(self):
        self.display_person()
        print("Role:",self.role)
emply=employee("Athira",28,"Software Developer")
emply.display_emply()