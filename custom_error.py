items = [1, 2, 3, 4, 5]

try:
    # Try to access the element at index 5 in the 'items' list.
    item = items[5]
    # If the index is valid, print the value of the element at index 5.
    print(item)
except Exception as e:
    # If an exception occurs during the 'try' block, catch it and print a custom error message.
    # The error message will be "Item does not exist in the list!!-" followed by the exception details (e).
    print("Item does not exist in the list!!-", e)
