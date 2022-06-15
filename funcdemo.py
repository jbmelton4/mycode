
'''Calculator'''
def sub(x, y):
    total= x - y
    return total

def add(x, y):
    total= x + y
    return total

def mult(x, y):
    total= x * y
    return total # Shows total as a result of above

                         #defining
                         #putting a block of code in python's MEMORY
def main(x, y):          # you can put def main(x, y=awesome) but it is a backup, it will default to what you have below on call
    print(f"{x} is {y}!")
    
    print(add(5,2))
    print(sub(5,2))
    print(mult(5,2))


#This is calling/executing your code!
main("James", "awesome") # This is positional arguments, so james will be x because it's the first variable on both instances.
#main()                  # multiple call functions can execute it multiple times. 
#main("awesome")         # Adding arguments to your function allows different configurations
