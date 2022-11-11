#Developer: Dimitrios Passias
#Issues: None
#Instructions: Import a file with the name "students.txt" that is used to collect data on the students and creates a menu for options to do with this data.

#Loads data from "students.txt and opens the lines
def load_data():
    new_File = open("students.txt", 'r')
    lines = new_File.readlines()
    students = []

   #for each line/student in this txt file is split then returns it in a list
    for line in lines:
        split_line = line.split("|")
        student = {
            'name': split_line[0],
            'student number': split_line[1],
            'credits': split_line[2],
            'gpa': split_line[3]
        }
        students.insert(0, student)
    return students

#adds the student according to the users input with the given credentials
def add_student(students):
    ##prints the questions for each credential
    student_name = input("Please enter the name of the new student:")
    student_number = input("Please enter the students number:")
    student_credits = input("Please enter the students current credits:")
    student_gpa = input("Please enter the students current GPA:")

    #puts it into a dictionary then adds it to the list
    new_student = {
        'name': student_name,
        'student number': student_number,
        'credits': student_credits,
        'gpa': student_gpa
    }
    students.append(new_student)

#Searches for students with a gpa higher than 3
def find_honor(students):
    print("Honor Students: ")

    #Each student is checked for their gpa
    for current_student in students:

        #if it is greater than 3 then it prints the students name
        if (float)(current_student['gpa']) > 3.0:
            print(f"{current_student['name']} ")

#checks the students gpas to see if their gpa was lower than 2
def find_probation(students):
    print("Probation Students: ")

    #each student is checked for their gpa
    for current_student in students:

        #if its lower than 2 then it prints the students name
        if (float)(current_student['gpa']) < 2.0:
            print(f"{current_student['name']} ")

#Checks the students if they have more than 25 credits
def find_masters(students):
    print("Master Students: ")

    #each student is checked for their credit
    for current_student in students:
        current_student_credits = float(current_student['credits'])

        #checks if the credits are less than 25 if so then the students name is printed
        if current_student_credits < 25:
            print(f"{current_student['name']}")

#Gives the options and performs each action according to the data and users choice
def perform_command(user_choice, students):
    if user_choice == '1':
        add_student(students)
    elif user_choice == '2':
        find_masters(students)
    elif user_choice == '3':
        find_probation(students)
    elif user_choice == '4':
        find_honor(students)
    elif user_choice == '5':
        exit(0)
    else:
        print("Invalid Selection, please choose 1-5")

#Prints the menu for the user
def print_menu():
    print("========Please selection from the following:=======")
    print("[1] Add a student")
    print("[2] Find masters students")
    print("[3] Find students on probation")
    print("[4] Find honors students")
    print("[5] End the program")
    print("====================================================")

#loads the data and asks for your selection while its still running
def main():
    student = load_data()
    while True:
        print_menu()
        user_selection = input("Your choice 1-5:")
        perform_command(user_selection, student)
main()