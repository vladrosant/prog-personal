import json
import datetime
import os

CREATINE_FILE = "creatine.json"

# Load existing creatine data from the file
try:
    with open(CREATINE_FILE, "r") as f:
        creatine_data = json.load(f)
except FileNotFoundError:
    creatine_data = []

def save_creatine():
    with open(CREATINE_FILE, "w") as f:
        json.dump(creatine_data, f)

def take_creatine():
    today = datetime.datetime.now().date().strftime("%m/%d/%Y")
    if today not in creatine_data:
        creatine_data.append(today)
        save_creatine()
        print("\n<>------------------------------<>\n\nYou've taken creatine today.")
    else:
        print("\n<>------------------------------<>\n\nDuplicated entry. Ignoring...")

def check_creatine_history():
    if len(creatine_data) == 0:
        print("\n<>------------------------------<>\n\nNo history found for creatine.")
    else:
        print("\n<>------------------------------<>\n\nCreatine intake history:\n")
        for date in creatine_data:
            print(date)
            continue

def system_clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system("clear")

while True:
    print("\n<>------------------------------<>\n")
    print("1. Take creatine")
    print("2. Check creatine history")
    print("3. Clear display")
    print("4. Quit")
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        take_creatine()
        
    elif choice == '2':
        check_creatine_history()

    elif choice == '3':
        system_clear()

    elif choice == '4':
        break
        
    else:
        print("Invalid choice. Please try again.")