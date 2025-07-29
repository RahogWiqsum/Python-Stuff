print("This is a calculator")
print(" ")
print(" ")
print(" ")


def Calculator():
    Operation = int(input("What would you like to do? 1. Addition 2. Subtraction 3. Multiplication 4. Division" ))

    if Operation == 1:
        Number1  = int(input("Enter your first number: "))
        Number2 = int(input("Enter your second number: "))
        Answer = Number1 + Number2
        print(Answer)
        CheckForContinue()
    elif Operation == 2:
        Number1  = int(input("Enter your first number: "))
        Number2 = int(input("Enter your second number: "))
        Answer = Number1 - Number2
        print(Answer)
        CheckForContinue()
    elif Operation == 3:
        Number1  = int(input("Enter your first number: "))
        Number2 = int(input("Enter your second number: "))
        Answer = Number1 * Number2
        print(Answer)
        CheckForContinue()
    elif Operation == 4:
        Number1  = int(input("Enter your first number: "))
        Number2 = int(input("Enter your second number: "))
        Answer = Number1 / Number2
        print(Answer)
        CheckForContinue()

def CheckForContinue():
    Continue = int(input("Again? 1. Yes 2. No "))

    if Continue == 1:
        print("Program finished")
    elif Continue == 2:
        Calculator()

Calculator()





