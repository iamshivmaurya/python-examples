from reportlab.pdfgen import canvas

from datetime import datetime
current = datetime.now()
current_day = current.strftime("%d")
current_month = current.strftime("%m")
current_year = current.strftime("%Y")
'''
 Write a program to generate voter card ID if the voter age is equal to or greater then 18 Years.
'''

# Create a new PDF file
def generate_pdf(output_filename, voter_card_data):
    # Initialize the canvas
    
    pdf = canvas.Canvas(output_filename,pagesize=[200,200])
    

    # Set font and size
    pdf.setFont("Helvetica", 12)

    # Write text at a specific position (x, y)
    y = 160
    for voter_data in voter_card_data:
        #print(voter_data)
        pdf.drawString(30, y, voter_data)
        y -= 20
        
    # Save the PDF
    pdf.save()

userList = {
    1: { 
        "name": "Rahul Maurya",
        "dob": "10/02/2020",
        "address": "Pryagraj U.P.",
        "word_num": "25"
    },
    2: { 
        "name": "Rajesh Maurya",
        "dob": "10/02/1950",
        "address": "Kanpur U.P.",
        "word_num": "26"
    },
    3: { 
        "name": "Ramu Yadav",
        "dob": "10/02/1993",
        "address": "Lucknow",
        "word_num": "27"
    },
    4: { 
        "name": "Rajesh Sharma",
        "dob": "10/02/1994",
        "address": "Rajiv Nagar,Haryana",
        "word_num": "28"
    },
    5: { 
        "name": "Monu Varma",
        "dob": "10/02/1960",
        "address": "Shantipuram Prayagraj",
        "word_num": "29"
    }
}
for user in userList.items():
    user_id = user[0]
    user_dob = datetime.strptime(user[1]['dob'], "%d/%m/%Y")
    dob_year = user_dob.strftime("%Y")
    age = int(current_year) - int(dob_year)
    user_name = user[1]['name']
    user_dob = user[1]['dob']
    user_address = user[1]['address']
    user_word_num = user[1]['word_num']

    if age >= 18 :
        voter_card_data = [
                "****Voter Card ID***",
                "Name : " + user_name,
                "DOB: " + user_dob,
                "Address: " + user_address,
                "Word No.:" + user_word_num
            ]

        file_name = f"voter_id_card_{user_id}.pdf"
        #print(file_name)
        generate_pdf(file_name, voter_card_data)
        #break

    
        