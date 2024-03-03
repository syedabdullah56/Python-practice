class employee:
    name="Harry"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
            return i
    def __str__(self):
        print(f'The name of employee is {self.name}')
        
    def __repr__(self):
        print(f'The name of employee is {self.name}')












a=employee()
print(a.__len__())
print(a.__str__())
print(a.__repr__())