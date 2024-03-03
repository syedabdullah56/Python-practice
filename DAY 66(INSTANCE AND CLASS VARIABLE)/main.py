class employee:
    # class variable
    count=0
    companyname="Apple"
    def __init__(self,name,position):
        # instance variable
        self.name=name
        self._raiseamount=2
        self.position=position
        employee.count=employee.count+1
    def showdetails(self):
        print(f'{self.name} is an employee of {self.companyname} and his\her position is {self.position} and his raise amount is {self._raiseamount} aand no of employees in company are {employee.count} ')
    
a=employee("Abdullah","Software engineer")
b=employee("Aliyan","Electrical engineer")
c=employee("Badar","Chemical engineer")
a.showdetails()
b.showdetails()
c.showdetails()
a.companyname="Microsoft"
a.showdetails()
