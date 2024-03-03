# getters
class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f'VALUE IS {self._value}')
    @property
    def value(self):
        return 10*self._value
    
obj=myclass(67)
obj.show()
obj.ten_value=67
# setters
@ten_value.setter
def ten_value(self,new_value):
    self._value=new_value/10
obj=myclass(67)
obj.ten_value=67
print(obj.ten_value)
obj.show()


