class User :
    'This Class define users to say \"Hello\"'
    name=""
    
    def __init__(self, name,height):
        self.name = name
        self.height=height
        
    def sayHello(self):
        print('Hello ',self.name,' ,This is your training course')
        print('Your Height is = ',self.height)

# create virtual objects
Sadegh = User("Sadegh",178)
Mohamad= User("Mohamad",175)
Hesam= User('Hesam',181)

# call methods owned by virtual objects
Sadegh.sayHello()
Mohamad.sayHello()
Hesam.sayHello()

print('--------------------------------Predefined Methods with the name of Class')
print("User.__doc__=",User.__doc__)
print("User.__module__=",User.__module__)
print("User.__name__=",User.__name__)

        
        

    
