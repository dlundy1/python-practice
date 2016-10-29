import os

def main():
    #Main Program Code
    print("Main Method")
    helloDude()
    os.system("cal")
    print(add(5,5))

def helloDude():
    #helloDude method
    print("Hello Dude, Function Test")

def add(x,y):
    #add function
    return x + y

if __name__ == "__main__":
    main()
