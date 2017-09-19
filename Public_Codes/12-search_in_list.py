var = "LowerCase"
print(var.lower())
print(var.upper())
print(var)
print("---------------------------------------------")

#-----------------------------------------------------
colors = ["Red", "Green" ,"Orange", "Red", "Yellow", "Green", "Blue"]
colorSelect = ""
while colorSelect.upper()!= "QUIT":
    colorSelect = input("Please type a color name: ")
    if (colors.count(colorSelect) >= 1):
        print("The color exists in the list!")
    elif (colorSelect.upper() != "QUIT"):
        print("The list doesn't contain the color.")
