num1 = float(input("Choose the first number: "))

operator = input("Choose an operator (+ - / *): " )

num2 = float(input("Choose a second number: "))

if operator == "+":
    res = num1 + num2
    print(res)
elif operator == "-":
    res = num1 - num2
    print(res)
elif operator == "/":
    res = num1 / num2
    print(res)
elif operator == "*":
    res = num1 * num2
    print(res)