# Take two lists of integers as input
list1 = input("Enter the first list of integers (space-separated): ").split()
list2 = input("Enter the second list of integers (space-separated): ").split()

# Convert string inputs to integers
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

# (a) Check if both lists are the same length
if len(list1) == len(list2):
    print("Both lists are of the same length.")
else:
    print("Lists are of different lengths.")

# (b) Check if sums of both lists are equal
if sum(list1) == sum(list2):
    print("Both lists have the same sum.")
else:
    print("Lists have different sums.")

# (c) Check for common values in both lists
common_values = set(list1) & set(list2)  # set intersection
if common_values:
    print("Common values found:", common_values)
else:
    print("No common values found.")
