import csv

# Define the CSV file name
file_name = "PSPORTS.csv"

def P_INSERT():
    try:
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            p_no = input("Enter Player Number: ")
            p_name = input("Enter Player Name: ")
            total_score = input("Enter Total Score: ")
            p_amount = input("Enter Amount received per month by the Player: ")

            writer.writerow([p_no, p_name, total_score, p_amount])
            print("Player record added successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def P_DISPI():
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            print("\nPlayer Records:")
            for row in reader:
                print("{:<10} {:<20} {:<15} {:<10}".format(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        print(f"{file_name} file not found.")

def P_SEARCH():
    try:
        p_no_search = input("Enter Player Number to search: ")
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[0] == p_no_search:
                    found = True
                    print("\nPlayer Details:")
                    print("{:<10} {:<20} {:<15} {:<10}".format(row[0], row[1], row[2], row[3]))
            if not found:
                print("Player not found with Player Number:", p_no_search)
    except FileNotFoundError:
        print(f"{file_name} file not found.")

def P_COPY():
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            with open("PCPSPORTS.csv", mode='w', newline='') as copy_file:
                writer = csv.writer(copy_file)
                for row in reader:
                    p_no, p_name, total_score, p_amount = row
                    if float(p_amount) >= 300000:
                        writer.writerow([p_no, p_name, total_score, p_amount])
                print("Player details copied to PCPSPORTS.csv where P_Amount >= 300000.")
    except FileNotFoundError:
        print(f"{file_name} file not found.")

def P_DELETE():
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            lines_to_keep = []
            for row in reader:
                p_no, p_name, total_score, p_amount = row
                if int(total_score) >= 25:
                    lines_to_keep.append(row)

            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines_to_keep)
            print("Player records with Total Score < 25 deleted.")
    except FileNotFoundError:
        print(f"{file_name} file not found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Insert Player Record")
        print("2. Display Player Records")
        print("3. Search for a Player")
        print("4. Copy Records (P_Amount >= 300000) to PCPSPORTS.csv")
        print("5. Delete Records (Total Score < 25)")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            P_INSERT()
        elif choice == "2":
            P_DISPI()
        elif choice == "3":
            P_SEARCH()
        elif choice == "4":
            P_COPY()
        elif choice == "5":
            P_DELETE()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

