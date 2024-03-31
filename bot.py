a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

operation = input("Что выбрать ? (+ , - , * , /)")
result = 0

if operation == "+":
  result = a + b
elif operation == "-":
  result = a - b
elif operation == "*":
  result = a * b
elif operation == "/":
  result = a / b

print(f"Рузультат: {result}")