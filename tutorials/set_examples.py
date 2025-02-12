set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}


'''
numbers = [1, 2, 3, 4, 3, 2, 5]
unique_numbers = set(numbers)  # Convert list to set to remove duplicates
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Convert back to a list if needed
unique_numbers_list = list(unique_numbers)
print(unique_numbers_list)  # Output: [1, 2, 3, 4, 5]

'''

"""

visitors = set()  # Start with an empty set

# Simulate visits
visitors.add("user1")
visitors.add("user2")
visitors.add("user3")
visitors.add("user1")  # Duplicate, won't be added

print(visitors)  # Output: {'user1', 'user2', 'user3'}
print(f"Total unique visitors: {len(visitors)}")  # Output: 3

"""