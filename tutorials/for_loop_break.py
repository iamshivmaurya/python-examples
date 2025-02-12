total_fund_amount = 2000000
per_student_fund = 50000
students_anual_income = {
    "A": 300000,
    "B": 200000,
    "C": 100000,
    "D": 300000,
    "E": 200000,
    "F": 100000,
    "G": 300000,
    "H": 200000,
    "I": 100000
}

# Using break to exit the loop
def send_money(name):
    print(f"Money sent to {name}'s account.")

for student in students_anual_income:
    if students_anual_income[student] >= 300000:  # Access the income for the student
        continue  # Skip sending money for students with >= 300000 income
    send_money(student)  # Pass student name to send_money
    

