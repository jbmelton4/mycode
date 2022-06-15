# In Python it is better to ask forgiveness than to ask permission.
# Setting it up this way can also be bad, as it doesn't define the error. You can replace it, so you need to add an exception

try: 
    num= int(input("Pick a number: \n"))
    print(100 / num)
    print("Will you see me on an error? Nope!")

# We can force an error with a SyntaxError
#    raise SyntaxError

# Adds an error for wrong number
except ValueError:
    print("Not a number!")

# Adds an error for dividing by zero
except ZeroDivisionError:
    print("Can't divide by 0.")

# Adds an error for any other issues.
except Exception as varname:
    print("There was an error we weren't expecting!", varname)

finally: #no matter what happens, run this
    print("blah blah")