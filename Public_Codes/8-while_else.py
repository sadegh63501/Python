correctPassword = "SokanAcademy"
password = input("Please enter the password --> ")
while password != correctPassword:
    if password == "I`ve forgotton the password":
        email = input("Please enter your email to sent you correct password --> ")
        print("The password has sent to",email)
        break
    password = input("Please try again and enter the correct password "+
                     "or type:I`ve forgotton the password --> ")
else:
    print("Welcome to SokanAcadmy.com") # Run if didn't exit loop with break
