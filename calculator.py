
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print("Welocme to the Calculator")
    from calculator_art import logo
    print(logo)
    num1=float(input("What's the first number?:"))
    choice='y'
    answer=num1
    for symbol in operations:
            print(symbol)
        
    while choice=='y':
        operation_symbol=input("Pick an operation from the lines above:")
        num2=float(input("What's the next number?:"))
        answer=operations[operation_symbol](answer,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice=input("Type 'y' to continue calculating with {answer} or type 'n' to to start a new calculation:")
        if choice=='n':
             calculator()
        

calculator()