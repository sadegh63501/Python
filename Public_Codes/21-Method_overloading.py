class Human:
    
    name=""
    
    def say_hello(self,name=None):
        self.name=name
        if self.name :   # or if name is not None:
            print('Hello',self.name)# print('Hello',name)
        else:
            print('Hello')

obj = Human()
obj.say_hello('Majid')
obj.say_hello()

