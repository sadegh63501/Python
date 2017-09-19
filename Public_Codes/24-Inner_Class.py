class Human:
    def __init__(self,name):
        self.name = name
        self.head = self.Head()
        self.brain = self.Brain()

    class Head:
        def talk(self):
            return "talking"

    class Brain:
        def think(self):
            return "thinking"

if __name__ == '__main__':#for execute Code only if the Script run independently and not running as a Module
    hesam = Human("Hesam")
    print(hesam.name)
    print(hesam.brain.think())
    print(hesam.head.talk())
        
