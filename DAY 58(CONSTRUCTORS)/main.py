class person:
    def __init__(self,n,o):
        print("HELLO WELCOME TO CODE")
        self.name=n
        self.occ=o
    def info(self):
            print(f"{self.name} is a {self.occ}")

a=person("Abdullah","Software engineer")
b=person("Aliyan","Electrical engineer")
c=person("Abdullah","Chemical engineer")
a.info()
b.info()
c.info()
