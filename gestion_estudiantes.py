import time


listStudents = {}
flag = True

def validateNumber(messages):
    while flag:
        numberId = input(messages)
        if numberId.isdigit() and int(numberId) > 0:
            return int(numberId)
        print("❌ Please enter a valid age greater than 0.")

def validateNotes(messages):
    while flag:
        try:
            note = float(input(messages))
            if 0 <= note <= 5:
                return note
            else:
                print("❌ Please, The note must be between 0 y 5.")
        except ValueError:
            print("❌ Please, Enter a number valid.")

def validateName(messeges):
    while flag:
        nameInput = input(messeges).strip()
        
        if not nameInput:
            print("❌ The name can't be empty.")
        elif nameInput.isdigit():
            print("❌ numbers are not accepted")
        else:
            return nameInput


def registerStudent():
    id = input("Enter the number ID: ").strip()
    if not id:
        print("❌ The ID can't be empty.")
        return False
    if id in listStudents:
        print("⚠️ There is already a student with that ID")
        return False

    name = validateName("Enter the student name: ")

    age = validateNumber("Enter the age Student:  ")

    notes = []
    print("Enter 3 notes:")
    for i in range(3):
        nota = validateNotes(f"Note {i+1}: ")
        notes.append(nota)

    listStudents[id] = {
        "name": name,
        "age": age,
        "notes": notes
    }
    
    print("✅ student successfully registered .\n")

def consultStudent():
    id = input("Enter the Id number: ").strip()
    student = listStudents.get(id)

    if student:
        average = sum(student["notes"]) / len(student["notes"])
        print(f"\n👤 Name: {student['name']}")
        print(f"🎂 Age: {student['age']}")
        print(f"📘 Notes: {student['notes']}")
        print(f"📊 Average: {average:.2f}\n")
    else:
        print("❌ Student not found.\n")

def updateNotes():
    id = input("Enter the Id number: ").strip()
    if id in listStudents:
        print("Enter the 3 new notes:")
        listNotes = []
        for i in range(3):
            Newnote = validateNumber(f"New note {i+1}: ")
            listNotes.append(Newnote)
        listStudents[id]["notes"] = listNotes
        print("✅ Notes updated successfully.\n")
    else:
        print("❌ Student not found.\n")

def deleteStudent():
    id = input("Enter the Id number: ").strip()
    if id in listStudents:
        del listStudents[id]
        print("✅ Student successfully removed.\n")
    else:
        print("❌ Student not found.\n")

def showStudent():
    if not listStudents:
        print("📭 There are no registered students.\n")
        return
    print("\n📋 List of student:")
    for id, datos in listStudents.items():
        average = sum(datos["notes"]) / len(datos["notes"])
        print(f"ID: {id} | Nombre: {datos['name']} | Edad: {datos['age']} | Promedio: {average:.2f}")
    
    
    
def printLate(text, delay=0.08):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    

def menu():
    while flag:
        print("===== MAIN MENÚ =====")
        print("1. Register student")
        print("2. consult student")
        print("3. Update notes")
        print("4. Delete student")
        print("5. See all students")
        print("6. Exit")
        print("====================")

        option = input("Enter an option: ").strip()

        match option:
            
            case "1":
                registerStudent()
            
            case "2":
                consultStudent()
                
            case "3":
                updateNotes()
                
            case "4":
                deleteStudent()
                
            case "5":
                showStudent()
                
            case "6":
                printLate("👋 ¡Thanks for using the system! See you soon!.....")
                break
            
            case _:
                print("❌ Option invalidates. try again.\n")

# Ejecutar el programa
menu()
