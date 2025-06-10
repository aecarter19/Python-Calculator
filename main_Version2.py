def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    op = input("Operation: ")
    x = float(input("First number: "))
    y = float(input("Second number: "))

    if op == "+":
        print("Result:", add(x, y))
    elif op == "-":
        print("Result:", subtract(x, y))
    elif op == "*":
        print("Result:", multiply(x, y))
    elif op == "/":
        print("Result:", divide(x, y))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()