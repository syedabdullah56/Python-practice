class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'My name is {self.name}')

class manager(employee):
     def __init__(self,name,salary):
        self.name=name
        self.salary=salary
     def show(self):
        print(f'My name is {self.name} and my salary is {self.salary}')

class programmer(manager):
      def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
      def show(self):
        print(f'My name is {self.name} and my salary is {self.salary} and I use {self.language}')
        employee.show()
        manager.show()

a=programmer("Abdullah",100000,"Python")
b=employee("Aliyan")
b.show()
c=manager("kane",100000)
a.show()


