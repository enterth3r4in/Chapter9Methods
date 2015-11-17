#Fun with methods
def sayHello():
    print("Hello, World!")

def oneArgument(var1):
    print("Hello, ", var1, "!")
    pass

#main
print("Main Started")
sayHello()
userName = input("Please enter your name: ")
oneArgument(userName)
print("Main Ended")