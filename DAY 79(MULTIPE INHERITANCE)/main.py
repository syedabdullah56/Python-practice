class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'My name is {self.name}')
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f'The dance is {self.dance}')
class danceremployee(employee,dancer):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance
    
a=danceremployee("Abdullah","robot dance")
a.show()

