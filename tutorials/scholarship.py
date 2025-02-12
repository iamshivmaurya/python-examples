# Scholarship Program
# Send scholarship to students' bank accounts

total_fund_amount = 2000000  # 20L
per_student_fund = 350000  # 250 Thousand

# Students Annual Income (will get from DB)
students_anual_income = {
    "A": 300000, 
    "B": 200000,
    # "C": 100000,
    # "D": 300000,
    # "E": 200000,
    # "F": 100000,
    # "G": 300000,
    # "H": 200000,
    # "I": 100000
}

def sendSms(mobile_number):
    print("SMS -> Your account credited!")

def bankAPISendMeney(account_details, money):
    print(f"Sending money to student account {account_details}. Rs {money}")
    return 1

# Function to send money
def send_money(student, account_details, mobile_number, per_student_fund):
    #print(f"Money sent to {student}'s account.")
    #
    money_send = bankAPISendMeney(account_details, per_student_fund)
    if(money_send):
        print(f"Money has been sent to {student}'s account. Rs: {per_student_fund}")
        sendSms(mobile_number)
    #SMS -> message send


# Distribute scholarship funds to eligible 
# {"A": 300000},

for student, income in students_anual_income.items():
    if income <= 300000:
        if total_fund_amount >= per_student_fund: #20,00,000 > 50,0000
            send_money(student, 100000001, 9999887766, per_student_fund)
            
            #print(f"Money sent to {student}'s account.")
            total_fund_amount = total_fund_amount - per_student_fund
            print("====")
        else:
            print("Insufficient funds to send scholarship.")
            break

print(f"Remaining fund amount: {total_fund_amount}")





