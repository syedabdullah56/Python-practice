class employee:
    company="Apple"
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'The name of employee is {self.name} and his company name is {self.company}')
    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany
a=employee("ABDULLAH")
a.changecompany("MICROSOFT")
a.show()
print(employee.company)
