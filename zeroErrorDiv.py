def div(a, b):
    # This function performs division of 'a' by 'b' and returns the result.
    return a / b

try:
    # Try to call the 'div' function with arguments 40 and 0.
    ans = div(40, 0)
    # If no exception occurs during the 'try' block, print the result of the division (which won't happen here).
    print(ans)
except Exception as e:
    # If a 'ZeroDivisionError' (or any other exception) occurs during the 'try' block,
    # catch it and print 0 instead of the actual result.
    print(0)
