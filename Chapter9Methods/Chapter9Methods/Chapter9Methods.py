#Fun with methods
def sayHello():
    print("Hello, World!")

def oneArgument(var1):
    print("Hello, ", var1, "!")

def twoArgument(var1, var2):
    print("Hello, ", var1, "! Your color is ", var2)

def valueReturned(var1, var2):
    return var1 + " has a " + var2

#main
print("Main Started")
sayHello()
userName = input("Please enter your name: ").strip()
color = input("Please pick your favorite color: ").strip()
twoArgument(userName, color)
userAnimal = input("Enter your favorite Animal: ")
print(valueReturned(userName, userAnimal))
print("Main Ended")