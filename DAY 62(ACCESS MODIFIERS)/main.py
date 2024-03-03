# public
class enemy:
    def __init__(self,health,gun):
        self.health=health
        self.gun=gun
    def show(self):
        print(f"Hi I am enemy and my health is {self.health} and my gun is {self.gun}")

a=enemy(100,"AK47")
b=enemy(90,"MAVERICK")
c=enemy(10,"BULLPUP")
a.show()
b.show()
c.show()

# private

class enemy1:
    def __init__(self,health,gun):
        self.__health=health
        self.__gun=gun
    def show(self):
        print(f"Hi I am enemy and my health is {self.__health} and my gun is {self.__gun}")

a=enemy1(100,"AK47")
b=enemy1(90,"MAVERICK")
c=enemy1(10,"BULLPUP")
a.show()
b.show()
c.show()
print(a._enemy1__gun) 
# it can be accessed my above method

# protected
class myperson:
    def __init__(self,name):
        self._name=name
    def name(self):
        print(f'My name is {self.name}')
e=myperson("Abdullah")
print(e._name)
