class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def show(self):
        return (f'{self.i}i +{self.j}j +{self.k}k')

    def __add__(self,x):
        return f'{self.i +x.i}i +{self.j+x.j}j +{self.k+x.k}k'



v=vector(3,5,6)
print(v.show())
e=vector(4,8,7)
print(e.show())
print(v+e)