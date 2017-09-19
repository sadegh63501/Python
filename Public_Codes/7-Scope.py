#Local Variables
print("---------------Local Vars-----------------")
name = "Sadegh"
print(name)
def setName():
    name = "Narges"
    print(name)
print(name)
setName()

print("--------------------------------")

def setName1():
    name = "Narges"
    
def getName1():
    name = "Puya"
    setName()
    return name

print(getName1())


print("---------------Global Vars-----------------")
#Global
def setScope():
    scope = "local"
    print(scope)
scope = "global"
setScope()
print(scope)

print("--------------------------------")

def setScope1():
    global scope1
    scope1 = "local"  # This is a global variable.
scope1 = "global"
setScope1()
print(scope1)

print("--------------------------------")

def setGlobalScope():
    global scope
    scope = "global" # this is the global

def setScope():
    scope = "local" # this is the local
    
def printScope():
    print(scope) # this is the global
    
scope = None # this is the global
setGlobalScope()
setScope()
printScope()
