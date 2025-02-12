from datetime import datetime, timedelta

# Given date in DD/MM/YYYY format
given_date = datetime.strptime("2025/02/10", "%Y/%m/%d")

# Calculate 60 days in the future and past
future_date = given_date + timedelta(days=60)
past_date = given_date - timedelta(days=60)

# Extract day, month, and year
print("Given Date:", given_date.strftime("%d/%m/%Y"))
print("\nFuture Date (+60 days):", future_date.strftime("%d/%m/%Y"))
print("  Day:", future_date.day)
print("  Month:", future_date.month)
print("  Year:", future_date.year)

print("\nPast Date (-60 days):", past_date.strftime("%d/%m/%Y"))
print("  Day:", past_date.day)
print("  Month:", past_date.month)
print("  Year:", past_date.year)
