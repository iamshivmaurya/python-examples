from datetime import datetime
import random

current_date = datetime.now()
print("Current Date And Time ", current_date)

current_year = current_date.strftime("%Y")

print(" current_year", current_year)

passenger_list = { 
    1: { 
        "name": "Shiv Maurya",
        "dob": "10/02/1988",
        "email": "skmaurya.ald@gmail.com",
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
        "dob": "10/02/2016",
        "email": "skmaurya3.ald@gmail.com",
        "mobile" : "998877665"
    },
    4: { 
        "name": "Rajesh Sharma",
        "dob": "10/02/1994",
        "email": "skmaurya2.ald@gmail.com",
        "mobile" : "998877665"
    },
    5: { 
        "name": "Rajesh Varma",
        "dob": "10/02/1950",
        "email": "skmaurya2.ald@gmail.com",
        "mobile" : "998877665"
    },
}


for passenger in passenger_list.items():
    #print(passenger[1]["dob"])#
    passenger_dob = datetime.strptime(passenger[1]['dob'], "%d/%m/%Y")
   # print(customer_dob)#
    passenger_year = passenger_dob.strftime("%Y")
    #print("Passenger BOY ", passenger_year)
    year_diff = int(current_year) - int(passenger_year)

    #print(f"Passanger \"{passenger[1]['name']}\" Age : {year_diff}")
    customer_email = passenger[1]['email']
    customer_name =  passenger[1]['name']

    seat_number = random.randint(10,20)
    otp = random.randint(100000,999999)
    print("otp", otp)
    coach = "B"+str(random.randint(1,20))

    # Train No. 12350 , total coachs  - 20 

    if year_diff <= 10 or year_diff >= 50:
        print(f"Hello {passenger[1]['name']}, \n Your seat alloweted in coach {coach} seat {seat_number} lower birth")
    #if current_year and year  or current_year and year :

