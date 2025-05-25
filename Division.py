while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero")
        continue
    else:
        print("Result:", result)
        break