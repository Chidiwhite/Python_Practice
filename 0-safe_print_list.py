def safe_print_list(my_list=None, x=0):
    # Handle the default behavior if 'my_list' is not provided.
    if my_list is None:
        my_list = []  # If 'my_list' is not provided, initialize an empty list.

    # Initialize a variable 'ret' to keep track of the number of successfully printed elements.
    ret = 0

    # Iterate through the range from 0 to 'x' (exclusive).
    for i in range(x):
        try:
            # Try to access and print the element at index 'i' from 'my_list'.
            print("{}".format(my_list[i]), end=" ")
            ret += 1  # Increment 'ret' for each successfully printed element.
        except IndexError:
            # If an IndexError occurs (i.e., 'my_list' is not long enough), break out of the loop.
            break

    # Print a new line to separate the printed elements from the rest of the output.
    print("")

    # Return the number of elements successfully printed.
    return ret

ans = safe_print_list(my_list=["neo", "leo", "theo", 4, 5], x=3)

# Print the number of elements successfully printed (the value returned by 'safe_print_list').
print(ans)