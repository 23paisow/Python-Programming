first = str(input("What is your first name? "))
last = str(input("What is your last name? "))
ID = int(input("Student ID: "))
schedule = ""
block = 1
print(f"*************************************************\n*\t\t\t\t\t\t*\n*\t{last},{first}\tID: {ID}\t\t*\n*\t\t\t\t\t\t*\n*************************************************\n*\t\t\t\t\t\t*")
while True:
    class1 = input("Enter the next class, STOP to end: ")
    if class1 == "STOP":
        break
    room = input("Enter the room number: ")
    schedule = f"*\tBlock {block}: {class1}\tRoom: {room}\t*"
    print (schedule)
    block = block+1
print("*************************************************\n*\t\t\t\t\t\t*\n*************************************************")