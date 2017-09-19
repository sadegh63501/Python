#---------------------------------
# range(stop)
for i in range(10):
    print(i)
print("---------------------------------------------------")


#---------------------------------
# range(start,stop)
for i in range(5,10):
    print(i)
print("---------------------------------------------------")


#---------------------------------
# range(start,stop,step)
for i in range(0,20,3):
    print(i)
print("---------------------------------------------------")


#---------------------------------
# range(start,stop,negativeStep)
for i in range(20,2,-2):
    print(i)
print("---------------------------------------------------")


#---------------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(i,"*",j," = ",i * j)
print("---------------------------------------------------")


#---------------------------------
n = int(input("Enter a number -->"))
for i in range(2, n):
    if n % i == 0:
        print(n, "is not a prime number")
        break
else:
    print(n, "is a prime number")


