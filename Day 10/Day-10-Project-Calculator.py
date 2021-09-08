from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}

def calculator():
  num1 = float(input("Enter first number: "))
  for operation in operations:
    print(operation)

  cont = True
  while cont == True:
    symbol = input("Pick an operation from the given options: ")
    num2 = float(input("Enter another number: "))
    calc_function = operations[symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")
    option = input(f"Would you like to continue calculating on {answer}? Type 'y' for Yes or 'n' for No: ")
    if option == "y":
      num1 = answer
    else:
      cont = False
      from replit import clear
      clear()
      calculator()

calculator()

    
