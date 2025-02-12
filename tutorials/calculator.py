def calculate(num1, num2, actions):
    match actions:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '%':
            return num1 % num2
        case '/':
            return num1 / num2

result = calculate(4, 2, "+")

print(f"Result = {result}")
