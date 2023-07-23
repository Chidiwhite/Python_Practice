def list_division(my_list_1, my_list_2, list_length):
    # Use a list comprehension and zip function to perform element-wise division of 'my_list_1' by 'my_list_2'.
    # The zip function pairs up elements from 'my_list_1' and 'my_list_2', and the list comprehension
    # calculates the division result for each pair and creates a new list 'list_length' containing the results.
    list_length = [m/n for m, n in zip(my_list_1, my_list_2)]
    
    return list_length  # Return the new list containing the division results.

# Call the 'list_division' function with 'my_list_1' set to [30, 20, 10],
# 'my_list_2' set to [6, 5, 2], and 'list_length' set to 87 (this argument is unused in the function).
# The function will perform element-wise division of the two lists and return a new list with the results.
new = list_division(my_list_1=[30, 20, 10], my_list_2=[6, 5, 2], list_length=87)

# Print the new list containing the division results.
print(new)
