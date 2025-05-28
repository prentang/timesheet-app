def add_entry(timesheet):
    date = input("Date (MM-DD-YYYY): ")
    hours = float(input("Hours worked: "))
    desc = input("Description: ")
    timesheet.append({"date": date, "hours": hours, "desc": desc})
    print("Entry added!\n")

def show_entries(timesheet):
    for entry in timesheet:
        print(f"{entry['date']}: {entry['hours']} hours - {entry['desc']}")

def main():
    timesheet = []
    while True:
        print("\n1. Add entry\n2. Show entries\n3. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_entry(timesheet)
        elif choice == '2':
            show_entries(timesheet)
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
