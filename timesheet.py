import json
import os

def load_timesheet(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_timesheet(filename, timesheet):
    with open(filename, 'w') as f:
        json.dump(timesheet, f, indent=2)

def add_entry(timesheet):
    date = input("Date (MM-DD-YYYY): ")
    hours = float(input("Hours worked: "))
    desc = input("Description: ")
    timesheet.append({"date": date, "hours": hours, "desc": desc})
    print("Entry added!\n")

def show_entries(timesheet):
    if not timesheet:
        print("No data")
    else:
        for idx, entry in enumerate(timesheet, 1):
            print(f"{idx}. {entry['date']}: {entry['hours']} hours - {entry['desc']}")

def edit_entry(timesheet):
    show_entries(timesheet)
    if not timesheet:
        return
    try:
        idx = int(input("Enter the timesheet number you would like to edit: ")) - 1
        if 0 <= idx < len(timesheet):
            entry = timesheet[idx]
            print(f"Editing: {entry['date']} - {entry['hours']} hours - {entry['desc']}")
            new_hours = input(f"New hours (current: {entry['hours']}): ")
            new_desc = input(f"New description (current: {entry['desc']}): ")
            if new_hours:
                entry['hours'] = float(new_hours)
            if new_desc:
                entry['desc'] = new_desc

            print ("Entry updated")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number, please")

def delete_entry(timesheet):
    show_entries(timesheet)
    if not timesheet:
        return
    try:
        idx = int(input("Enter entry number you wish to delete: ")) - 1
        if 0 <= idx < len(timesheet):
            removed = timesheet.pop(idx)
            print(f"Deleted the following: {removed['date']} - {removed['hours']} hours - {removed['desc']}")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number, please")

def main():
    filename = "timesheet.json"
    timesheet = load_timesheet(filename)
    while True:
        print("\n1. Add entry\n2. Show entries\n3. Edit Entry\n4. Delete Entry\n5. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_entry(timesheet)
            save_timesheet(filename, timesheet)
        elif choice == '2':
            show_entries(timesheet)
        elif choice == '3':
            edit_entry(timesheet)
            save_timesheet(filename, timesheet)
        elif choice == '4':
            delete_entry(timesheet)
            save_timesheet(filename, timesheet)
        elif choice == '5':
            save_timesheet(filename,timesheet)
            print("Thank you")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
