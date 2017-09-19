#----------------------------------
list1=[]
print("lenght of list1 = ",len(list1))

list1.append("egg")
print("lenght of list1 = ",len(list1))
print("list1 = ",list1)

list1.append("meet")
list1.append("tea")
list1.append("rice")
print("lenght of list1 = ",len(list1))
print("list1 = ",list1)

print(list1[2])

list1.insert(2,"bread")
print("list1 = ",list1)

list2 = list1.copy()
print("list2 = ",list2)

list2.remove("rice")
print("list2 = ",list2)

list1.extend(list2)
print("list1 = ",list1)

print(list1.pop())
print("list1 = ",list1)

list1.clear()
print("list1 = ",list1)
