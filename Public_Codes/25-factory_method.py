class Car :
    def factory(type):
        if type=="RaceCar" :
            return RaceCar()
        elif type=="Van" :
            return Van()
        else :
            print("Bad car creation: " + type)    


class RaceCar(Car):
    def drive(self):
        print("Racecar driving.")

class Van(Car):
    def drive(self):
        print("Van driving.")

obj = Car.factory("Van")
obj.drive()
obj = Car.factory("RaceCar")
obj.drive()
#obj = Car.factory("Motoe")
#obj.drive()


    
