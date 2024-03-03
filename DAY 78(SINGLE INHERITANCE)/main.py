class animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("Sound made by the animals")
    def show(self):
        print(f"MY NAME IS {self.name}")
class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name="Dog")
        self.breed=breed
    def make_sound(self):
        print("BARK!")
    def show(self):
        print(f"MY NAME IS {self.name}")
class cat(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name="cat")
        self.breed=breed
    def make_sound(self):
        print("MEOWW!")
    def show(self):
        print(f"MY NAME IS {self.name}")

a=cat("Kitty","persian")
b=dog("dobby","bulldog")
c=animal("dog")
a.make_sound()
b.make_sound()
c.make_sound()
a.show()
b.show()
c.show()