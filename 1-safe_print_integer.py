def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Try to format and print 'value' as an integer.
        return True  # Return True if successful.
    except Exception as e:
        # If there's an exception, print an error message with the exception details.
        print(str(value) + " is not an integer:", e)


new = safe_print_integer(10)  # Call the function with 'value' set to 10.
print(new)  # Print the return value of the function.
