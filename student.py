students=[]
#save students in text file
def save_student():
    file=open("students.txt","w")
    for student in students:
        data=(
            student["roll"]+","+
            student["name"]+","+
            student["branch"]+","+
            student["cgpa"]+"\n"
                    )
        file.write(data)
    file.close()
    #loadingstudents from text file
def load_students():
    file=open("students.txt","r")
    for line in file:
        line.strip()
        if line=="":
            continue
        data=line.split(",")  
        student={
            "roll":data[0],
            "name":data[1],
            "branch":data[2],
            "cgpa":data[3]

        }  
        students.append(student)
    file.close()

#adding new students

def add_student():
    print("\n --Add students--")
    roll=input("enter you roll No:")
    name=input("enter your Name:")
    branch=input("enter you branch:")
    cgpa=input("enter CGPA:")

    student={
        "roll":roll,
        "name":name,
        "branch":branch,
        "cgpa":cgpa
    }
    students.append(student)
    save_student()
    print("student added")

#showing all students
def view_students():
    print("\n --students list--")  
    if len(students)==0:
        print("No studets")
        return

    for student in students:
        print("-----------------------") 
        print("Roll no:",student["roll"]) 
        print("Name:",student["name"])
        print("Branch:",student["branch"])
        print("CGPA:",student["cgpa"])
        print("All student printed")
        print("---------------------")


def search_student():
    print("\n search Student")
    roll=input("enter your Roll no:")
    for student in students:
        if student["roll"]==roll:
            print("\n Student found: current data is :")
            print("Name:",student["name"])
            print("Branch:",student["branch"])
            print("CGPA:",student["cgpa"])      


def update_student():
    print("\n --update studentt--")
    roll=input("Enter the Roll No:")
    for student in students:
        if student["roll"]==roll:
            print("\n Student found: current data is :")
            print("Name:",student["name"])
            print("Branch:",student["branch"])
            print("CGPA:",student["cgpa"])

            print("\n Enter new Details")
            student["name"]=input("Enter Name:")
            student["branch"]=input("Enter Branch:")
            student["cgpa"]=input("Enter CGPA:")

            save_student()
            print("\n Student update successfuly")
            return
    print("\n Student not found")                   

def delete_student():
    print("\n Delete student--")
    roll=input("Enter Roll No:")

    for student in students:
        if student["roll"]==roll:
            student.remove(student)
            save_student()
            print("Deleted successfully")
            return            
                