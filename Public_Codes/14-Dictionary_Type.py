menu = {"breakfast":"egg", "lunch":"rice", "dinner":"salad"}
print(menu)
print("The Launch is : ", menu['lunch'])
print("The Keys are : ",menu.keys())

print("-----------------------------------------------------")
for item in menu.keys():
	print ("We have " + menu[item] + " for " + item + ".")

print("---------------------------------------Change the Menu")
menu["lunch"] = "meat"
print(menu)

print("---------------------------------------Change the Menu")
menu.update({"lunch":"rice" , "snack":"nut"})
print(menu)
