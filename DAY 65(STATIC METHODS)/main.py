class person:
    def __init__(self,name,country,profession):
        self.name=name
        self.country=country
        self.profession=profession
    def show(self):
        print(f'My name is {self.name} and my country is {self.country} and I am A {self.profession}')
    @staticmethod
    def add(a,b):
        return a+b
    
a=person("Abdullah","Pakistan","Software engineer")
a.show()
print(a.add(7,2))