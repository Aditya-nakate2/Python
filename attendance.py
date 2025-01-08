# program to calculate students attendance 
# name and attendace count of students in a class
std_lst = {"ashish":15,
           "nominath":10,
           "pushkar":5,
           "dhiraj":7,
           "sarthak":8,
            "vivek":9,
            "abhijeet":11,
            "aditya":12}

def add_attendace(): #function to add attendance of a student
    name = str(input("Enter student name: ").lower())
    if name in std_lst:
        std_lst[name] += 1
        print("Attendance updated for",name,"succusfully")
    else:
        print("invalid name try again")
    
def show_attendance(): #function to show attendance of all students
    for name,attendance in std_lst.items():
        print(f"{name} : {attendance}")

def show_one_std(): #function to show attendance of one student
    name = str(input("Enter student name: "))
    if name in std_lst:
        print(f"{name} is present for {std_lst[name]} times in a month")
    else:
        print("invalid name try again")
    
def avg_attendance(): #function to show average attendance of all students
    total_attendance = sum(std_lst.values())
    total_students = len(std_lst)
    avg = total_attendance / total_students
    print(f"Average attendance of students is {avg}")

while True:
    print("\n1.Add attendance\n2.Show all students attendance\n3.show one student attendance\n4.Average attendance\n5.exit")
    choice = int(input("Enter your choice: "))
    try :
        if choice == 1:
            add_attendace()
        elif choice == 2:
            show_attendance()
        elif choice == 3:
            show_one_std()
        elif choice == 4:
            avg_attendance()
        elif choice == 5:
            break
        else:
            print("invalid choice try again")
    except ValueError:
        print("Invalid input try again")  # if user enters something other than 1,2
        continue  # and it will ask again for choice