class employees:
    def __init__(self,name,id,company,position):
        self.name=name
        self.id=id
        self.company=company
        self.position=position
    def showdetails(self):
        print(f'{self.name} is a {self.position} in {self.company} and his id is {self.id}')


a=employees("Abdullah",421,"Microsoft","Senior developer")
b=employees("Aliyan",422,"Apple","Electrical engineer")
c=employees("Badar",423,"Fauji fertilizer","Chemical engineer")
a.showdetails()
b.showdetails()
c.showdetails()

class manager(employees):
    def show(self):
        self.salary=10000000
        self.car="Mercedes Benz"
        self.language="PYTHON"
        print(f'I am a manager and my salary is {self.salary} and i have {self.car} and I use {self.language}')

d=manager("Syed Abdullah",425,"Microsoft","Most Senior developer")   
d.showdetails()
d.show()
