def safe_print_division(a, b):
    try:
        div = a / b  # Try to perform the division of 'a' by 'b'.
    except ZeroDivisionError:
        # If 'b' is zero, a ZeroDivisionError occurs.
        div = None
        print("Error: Cannot divide by zero.")
    except TypeError:
        # If the types of 'a' and 'b' are not compatible for division, a TypeError occurs.
        div = None
        print("Error: Invalid operand types for division.")
    finally:
        # The code inside the 'finally' block will always execute, regardless of exceptions.
        # Here, we print the result of the division (including 'None' if there was an error).
        print("Inside result: {}".format(div))

    return div  # Return the result of the division (None if there was an error).

div = safe_print_division(12,0)
print(div)

#extra code example
try:
    # Raise a custom Exception with arguments 'spam' and 'eggs'.
    raise Exception('spam', 'eggs')
except Exception as inst:
    # Catch the raised Exception and handle it.
    print(type(inst))     # Print the type of the Exception (Exception class).
    print(inst.args)      # Print the arguments passed when raising the Exception ('spam', 'eggs').
    print(inst)           # Print the Exception object, which shows its type and arguments.
                         
    x, y = inst.args      # Unpack the Exception arguments into variables 'x' and 'y'.
    print('x =', x)       # Print 'x' ('spam' in this case).
    print('y =', y)       # Print 'y' ('eggs' in this case).
