print("---------------------------Private Method")
class Car:
 
    def __init__(self):
        self.__updateSoftware()
 
    def drive(self):
        print('driving')
 
    def __updateSoftware(self):
        print('updating software')
 
redcar = Car()
redcar.drive()
redcar._Car__updateSoftware() 

print("---------------------------Private Variable")
class Car1:
 
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
 
    def drive(self):
        print('driving.maxspeed ' + str(self.__maxspeed))
 
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
 
redcar = Car1()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
