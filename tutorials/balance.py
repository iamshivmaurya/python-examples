cartNo = int(input("Enter your card no. : "))

print(type(cartNo))
#1001
metroCards = { 
    1001 : 'Rs.200', 
    1002 : "Rs.30", 
    1003 : 'Rs.2000',
    1004 : 'Rs.4000',
    1005 : 'Rs.1000'
}

# Check if a key exists
if cartNo in metroCards: #true Or false
    print("Your balance is:", metroCards[cartNo])
else:
    print("Card number not found.")
