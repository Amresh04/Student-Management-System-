import student

while True:
    print("\n ----")
    print("STUDENT MANAGEMENT SYSTEM")

    print("1.Add student")
    print("2.View student")
    print("3.Update your Details")
    print("4.Delete student")
    print("5.Search a student")
    print("6.Exit")

    choise=input("Enter your choise:")

    if choise=="1":
        student.add_student()
    elif choise=="2":
        student.view_students()
    elif choise=="3":
        student.update_student()

    elif choise=="4":
        student.delete_student() 

    elif choise=="5":
        student.search_student()       

    elif choise=="6":
        print("Thank you")
        break
    else:
        print("INVALID CHOISE !")        