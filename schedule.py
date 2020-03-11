while True:
    first = str(input("What is your first name? "))
    last = str(input("What is your last name? "))
    ID = int(input("Student ID: "))
    class1 = str(input("Enter your class! Enter STOP to end: "))
    if class1 == "STOP":
        break
    rm1 = int(input("Enter room number of the class: "))

    class2 = str(input("Enter your class! Enter STOP to end: "))
    rm2 = int(input("Enter room number of the class: "))
    if class2 == "STOP":
        break

    class3 = str(input("Enter your class! Enter STOP to end: "))
    rm3 = int(input("Enter room number of the class: "))
    if class3 == "STOP":
        break

    class4 = str(input("Enter your class! Enter STOP to end: "))
    rm4 = int(input("Enter room number of the class: "))
    if class4 == "STOP":
        break

    class5 = str(input("Enter your class! Enter STOP to end: "))
    rm5 = int(input("Enter room number of the class: "))
    if class5 == "STOP":
        break
    class6 = str(input("Enter your class! Enter STOP to end: "))
    rm6 = int(input("Enter room number of the class: "))
    if class6 == "STOP":
        break

    print("*************************************************\n*\t\t\t\t\t\t*\n*\t   {}, {}\tID: {}\t*\n*                                               *\n*************************************************\n*\t\t\t\t\t\t*\n*\tBlock 1: {}\tRoom: {}\t*\n*\tBlock 2: {}\tRoom: {}\t*".format(last, first, ID, class1, rm1, class2, rm2, class3, rm3, class4, rm4, class5, rm5, class6, rm6 ))
    break