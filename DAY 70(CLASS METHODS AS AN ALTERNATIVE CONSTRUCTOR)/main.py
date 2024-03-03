class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(f"Name of employee is {self.name} and his salary is {self.salary}")
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
e=employee("Abdullah",160000)
e.show()
string="Usman-180000"
f=employee.fromstr(string)
f.show()