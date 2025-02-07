
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

print("Select operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice(1/2/3/4):")

    if choice in ("1", "2", "3", "4"):
        try:
            f1 = float(input("Enter first number: "))
            f2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input.Enter a valid number.")
            continue

        if choice == "1":
            print(f1, "+", f2, "=", add(f1, f2))

        elif choice == "2":
            print(f1, "-", f2, "=", sub(f1, f2))

        elif choice == "3":
            print(f1, "*", f2, "=", mul(f1, f2))

        elif choice == "4":
            print(f1, "/", f2, "=", div(f1, f2))

        next_calculation = input("Next calculation: (yes/no)")
        if next_calculation == "no":
            break
        else:
            print("Invalid input.")













