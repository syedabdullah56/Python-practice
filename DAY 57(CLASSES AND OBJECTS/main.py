class person:
    name="Abdullah"
    occupation="Software Engineer"
    company="Microsoft"
    
    def info(self):
        print(f"{self.name} is a {self.occupation} and its company is {self.company}")

a=person()
print(a.name)
print(a.occupation)
b=person()
c=person()
c.name="Aliyan"
c.occupation="Electrical engineer"
c.company="Apple"
b.name="Badar"
b.occupation="Chemical engineer"
b.company="Engro"
a.info()
b.info()
c.info()
