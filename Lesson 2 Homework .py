#Hello World Assignment
def main():

    greeting = "Hello, world!"
    
    userName = "Top"
    birthYear = 2000
    exactAge = 24.6121
    #24 years, 7 months, 10 days, 12 hours and 27 minutes.
    codeGod = False 
    #not yet ;)
    
    age = int(exactAge)
    name = str(input("What's Your name? "))
    
    print(f"{name} says... \n{greeting}")

if __name__ == "__main__":
    main()
