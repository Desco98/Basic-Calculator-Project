def add():
    a = int(input("First No.: "))
    b = int(input("Second No.: "))
    answer = a + b
    print(f"{a} + {b} = {answer}")

def sub():
    a = int(input("First No.: "))
    b = int(input("Second No.: "))
    answer = a - b
    print(f"{a} - {b} = {answer}")

def mul():
    a = int(input("First No.: "))
    b = int(input("Second No.: "))
    answer = a * b
    print(f"{a} * {b} = {answer}")

def div():
    a = int(input("First No.: "))
    b = int(input("Second No.: "))
    answer = a / b
    print(f"{a} / {b} = {answer}")

while True:
    print('''
    INSTRUCTIONS:
    A is for Addition
    B is for Subtraction
    C is for Multiplication
    D is for Division
    E is to Quit''')
    operator = input("Choose Operator: ")

    if operator == "A" or operator == "a":
        add()
    elif operator == "B" or operator == "b":
        sub()
    elif operator == "C" or operator == "c":
        mul()
    elif operator == "D" or operator == "d":
        div()
    elif operator == "E" or operator == "e":
        print("Program Ended")
        quit()
    else:
        print("Operator not found, Please read the instructions")