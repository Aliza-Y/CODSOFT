
print("Choose any arithmetic operation you want to perform: ")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

Choice = int(input("Choose an operation: "))

if (Choice in [1, 2, 3, 4]):

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if (Choice == 1):
        result = num1 + num2
    elif (Choice == 2):
        result = num1 - num2
    elif (Choice == 3):
        result = num1 * num2
    elif (Choice == 4):
        result = num1 // num2           
else:
    print("Invalid Operation!")  
print("Result: {} ".format(result))
