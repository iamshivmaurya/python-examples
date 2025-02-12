from datetime import datetime
from dateutil.relativedelta import relativedelta

# Define two dates
date1 = datetime(2025, 2, 10)
date2 = datetime(2000, 2, 10)

# Calculate the difference in years
difference = relativedelta(date1, date2)

# Print the difference
print(f"Difference: {difference.years} years")
