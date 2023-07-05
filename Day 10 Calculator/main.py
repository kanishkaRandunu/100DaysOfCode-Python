from replit import clear
from art import logo

def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def divide(n1,n2):
  return n1/n2

def multiply(n1,n2):
  return n1*n2

operations = {
  "+": add, 
  "-": substract,
  "/": divide,
  "*": multiply 
}

def calculator():
  print(logo)
  
  num1 = float(input("enter the first number: "))
  cont_status = True
  
  while cont_status:
    for symbol in operations:
      print(symbol)
    
    operation_selcted = operations[input("Select your operation: ")]
    num2  = float(input("enter the next number: "))
    
    answer = operation_selcted(num1, num2)
    print(answer)
  
    cont_or_new = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
  
    if cont_or_new == "y":
      num1 = answer
    elif cont_or_new == 'n':
      cont_or_new = False 
      clear()
      calculator()

calculator()

  