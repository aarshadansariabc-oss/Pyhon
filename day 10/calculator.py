
#Calculator
from logo import logo
#Add
def add(n1, n2):
    return n1+n2

#Substract
def Sub(n1, n2):
    return n1-n2

#Multiplication
def Multi(n1, n2):
    return n1*n2

#divide
def divide(n1, n2):
    return n1/n2


Operation = {
        "+" :  add,
        "-" :  Sub,
        "*" :  Multi,
        "/" :  divide
    }
print(logo)
def calculator():
    num1= int(input("Enter the first number : "))
    
    Should_continure = False
    for symbol in Operation:
        print(f"{symbol}")

    while not Should_continure:

        Operation_sybol = input("Pick an operatoin : ")
        num2 = int(input("Enter your next number : "))

        calculation_symbol = Operation[Operation_sybol]
        answer = calculation_symbol(num1,num2)

        print(f"{num1} {Operation_sybol} {num2} = {answer}")

        r =  input(f"Type 'y' to continue calculation with {answer},or 's' to start frong begining or type'n' to eixt : ").lower()
        if r == 'y':
            num1 = answer
        elif r == 's':
            calculator()
        else:
            Should_continure = True
        
        
calculator()