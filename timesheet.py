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

def main():
    filename = "timesheet.json"
    timesheet = load_timesheet(filename)
    while True:
        print("\n1. Add entry\n2. Show entries\n3. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_entry(timesheet)
            save_timesheet(filename, timesheet)
        elif choice == '2':
            show_entries(timesheet)
        elif choice == '3':
            save_timesheet(filename, timesheet)
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
