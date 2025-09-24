import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculation(n1, oper, n2):
    if oper in operations:
        result = operations[oper](n1, n2)
        if result is not None:
            print(f"{n1} {oper} {n2} = {result}")
        return result
    else:
        print("Invalid operator.")
        return None


while True:
    try:
        num_1 = float(input("Enter first number: "))
    except ValueError:
        print("Enter valid number!")
        continue

    print("Available operations:")
    for symbol in operations:
        print(symbol)

    operator = input("Enter an operator: ")
    if operator not in operations:
        print("Invalid operator!")
        continue

    try:
        num_2 = float(input("Enter second number: "))
    except ValueError:
        print("Enter valid number!")
        continue

    result = calculation(num_1, operator, num_2)
    if result is None:
        continue

    while True:
        choice = input("Enter 'y' to continue with result, 'n' for new calculation, 'e' to exit: ").lower()

        if choice == "y":
            num_1 = result
            print(f"Starting with {result}")
            
            while True:
                operator = input("+ \n- \n* \n/ \nEnter an operator: ")
                if operator in operations:
                    break
                print("Invalid operator!")

            try:
                num_2 = float(input("Enter next number: "))
            except ValueError:
                print("Enter valid number!")
                continue

            result = calculation(num_1, operator, num_2)

        elif choice == "n":
            print("Starting a new calculation...\n")
            break
        elif choice == "e":
            print("Exiting calculator. Goodbye!")
            exit()
        else:
            print("Invalid choice!")
