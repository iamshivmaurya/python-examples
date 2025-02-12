from datetime import datetime

# Input date string
date_string = "10/02/1988"

print(datetime.now())

# Convert to datetime object
date_object = datetime.strptime(date_string, "%d/%m/%Y")  # Format: DD/MM/YYYY

print("Date object:", date_object)
print("Year:", date_object.year)
print("Month:", date_object.month)
print("Day:", date_object.day)
