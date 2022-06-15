def smash(x):
    if x == ('smash'):
        print("Correct.")
        return True
    else:
        print("Incorrect.")
        return False

def smashorslash():
    print("Does Hulk smash or slash?")
    x=input()
    print(smash(x))

if __name__ == "__main__":
    smashorslash()

