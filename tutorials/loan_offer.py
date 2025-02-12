'''
Write a programe to send load offer on the customer birthday befor one day.
'''
from datetime import datetime
import send_mail
current = datetime.now()

#print(current)

current_day = current.strftime("%d")
current_month = current.strftime("%m")

customersList = {
    1: { 
        "name": "Shiv Maurya",
        "dob": "10/02/1988",
        "email": "skmaurya.ald@gmail.com"
        "mobile" : "998877665"
    },
    2: { 
        "name": "Rajesh Maurya",
        "dob": "10/02/1994",
        "email": "skmaurya2.ald@gmail.com",
        "mobile" : "998877665"
    },
    3: { 
        "name": "Ramesh Maurya",
        "dob": "10/02/1993",
        "email": "skmaurya3.ald@gmail.com",
        "mobile" : "998877665"
    }
    4: { 
        "name": "Rajesh Sharma",
        "dob": "10/02/1994",
        "email": "skmaurya2.ald@gmail.com",
        "mobile" : "998877665"
    },
    4: { 
        "name": "Rajesh Varma",
        "dob": "10/02/1994",
        "email": "skmaurya2.ald@gmail.com",
        "mobile" : "998877665"
    },
}

for customer in customersList.items():
    #print(customer[1]['dob'])
    customer_dob = datetime.strptime(customer[1]['dob'], "%d/%m/%Y")
    #print(customer_dob)
    month = customer_dob.strftime("%m")
    day = customer_dob.strftime("%d")

    customer_email = customer[1]['email']
    customer_name = customer[1]['name']
    if current_month == month or current_day == day:
        #send_mail.send(customer_email, customer_name)
        #send_mail.hello(customer_name)
        print("=====================================")


# Loop through customersList and read dob
#for customer_id, customer_info in customersList.items():
# print(f"Customer ID: {customer_id}, DOB: {customer_info['dob']}")
