# dir
x=[1,2,3,4]
print(dir(x))
print(x.__add__)
# dict
class person:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def show(self):
        print(f"I am {self.name} and my height is {self.height}")

a=person("abdullah","5'7''")
a.show()
print(a.__dict__)

# help
print(help(person))