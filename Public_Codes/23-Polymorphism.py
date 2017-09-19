print("------------------------")
print("Polymorphism  With Function")
print("------------------------")
class Animal:
    def __init__(self,name):
        self.name=name

    def introduceUS(self):
        print("We Are ALL ANIMALs")

class Cat(Animal):
    def voice(self):
        print("My Voice Is : Mu")

class Dog(Animal):
    def voice(self):
        print("My Voice Is : Woow")

def animaintroduce(animaltype):
    animaltype.introduceUS()
    print("My Name is : ",animaltype.name)
    animaltype.voice()
    
catobj=Cat("Cat")
dogobj=Dog("Dog")

animaintroduce(catobj)
animaintroduce(dogobj)

print("------------------------")
print("Polymorphism  With Class")
print("------------------------")

class Car:
    def __init__(self,name):
        self.name=name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class SportsCar(Car):
    def drive(self):
        return "Sportscar driving!"
    def stop(self):
        return "Sportscar braking!"

class Truck(Car):
    def drive(self):
        return "Truck driving slowly because heavily loaded."
    def stop(self):
        return "Truck braking!"

cars = [Truck("BananaTruck"),
        Truck("OrangeTruck"),
        SportsCar("X3")]
for car in cars :
    print(car.name + ":" + car.drive()+car.stop())

print(type(cars))

    
        
