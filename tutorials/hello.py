colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

def square(x):
    return x ** 40

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(squared_numbers)
