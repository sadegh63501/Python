class MyClass:
    Size = 0

myInstance = MyClass()

print(myInstance.Size)

myInstance.Size = 100
print(myInstance.Size)


class Shape:
    size = 2
    def __init__(self, name, color):
      self.name = name
      self.color = color

shape1 = Shape('Circle','Yellow')
shape2 = Shape('Square','Green')

print(shape1.name)
print(shape2.color)

shape1.color = 'blue'
shape1.radius = 20
del shape1.name

print(shape1.color)
print(shape1.radius)
#print(shape1.name)

print(hasattr(shape1,'color'))
print(getattr(shape1,'color'))
setattr(shape2, 'radius', 8) # Set attribute 'radius' at 8
print(getattr(shape2,'radius'))
