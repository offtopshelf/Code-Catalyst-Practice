

def main():
    
#Grading System
    userGrade = int(input("Enter in your grade (0-100):"))
    print("")
    
    if userGrade >= 90:
        print("You have an A!")
    elif userGrade >= 80:
        print("You have a B!")
    elif userGrade >= 70:
        print("You have a C.")
    elif userGrade >= 60:
        print("You have a D.")
    else:
        print("You have a F!")
    
    match userGrade:
        case userGrade if userGrade >= 90:
            print("Keep up the good work!")
        case userGrade if userGrade >= 80:
            print("You're doing great!")
        case userGrade if userGrade >= 70:
            print("Keep trying!")
        case userGrade if userGrade >= 60:
            print("We believe you can achieve more!")
        case _:
            print("We can do better together!")

#For/While Loops    
    x = 0
    y = range(11)
    
    while x <= 10:
        print(x)
        x += 1
    
    for i in y:
        print(i)

if __name__ == "__main__":
    main()
    