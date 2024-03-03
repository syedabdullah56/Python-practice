class parent:
    def parent_method(self):
        print("This is a parent method")
class child(parent):
    def child_method(self):
        print("this is a child method")
        super().parent_method()

a=child()
a.child_method()
a.parent_method()

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f'MY NAME IS {self.name} and my id is {self.id}')
class progrmammer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
    def show(self):
        print(f"I am a programmer and i use {self.lang}")
a=progrmammer("Abdullah",421,"Python")
b=employee("Aliyan",420)

a.show()
b.show()



        
        