import os

def create():
    while True:
        choice = input("Do you want to create a new file or continue with an existing file? (create/continue): ").lower()
        if choice == "create":
            file_name = input("File name: ")
            try:
                with open(file_name, "x") as file:
                    file.write("floor,place,row,name,author\n")
                    print(f"File {file_name} created successfully!")
                    return file_name
            except FileExistsError:
                print("File already exists! Using the existing file.")
                return file_name
        elif choice == "continue":
            file_name = input("File name: ")
            if os.path.exists(file_name):
                return file_name
            else:
                print("File does not exist! Try again.")

def add(floor, place, row, name, author):
    file_name = create()
    if not file_name:
        return  
    with open(file_name, "r+") as file:
        lines = file.readlines()
        if int(row) > 10:
            print("Row number should be less than 10")
            return
        counter = 0
        for line in lines[1:]:  
            if name in line:
                print(f"Book with name {name} already exists!")
                return
            line_parts = line.strip().split(",")
            if line_parts[0] == floor and line_parts[1] == place and line_parts[2] == row:
                counter += 1
        if counter >= 10:
            print("You can't add more books in this row")
            return
        file.write(f"{floor},{place},{row},{name},{author}\n")
        print("Successfully added.")

def show_stats(place):
    file_name = create()
    if not file_name:
        return
    with open(file_name, "r") as file:
        next(file)  
        counter = sum(1 for line in file if line.strip().split(",")[1] == place)
    print(f"There are {counter} books in {place}")
def delete_book(name):
    file_name = create()
    if not file_name:
        return False
    temp_file = "temp.txt"
    found = False
    with open(file_name, "r") as file, open(temp_file, "w") as temp:
        for line in file:
            if name not in line:
                temp.write(line)
            else:
                found = True
    if found:
        os.replace(temp_file, file_name)
        print(f"Book with name '{name}' deleted successfully!")
        return True
    else:
        os.remove(temp_file)
        print(f"Book with name '{name}' not found.")
        return False
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Show books in a place")
        print("3. Delete a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            floor = input("Enter floor: ")
            place = input("Enter place: ")
            row = input("Enter row: ")
            name = input("Enter book name: ")
            author = input("Enter author's name: ")
            add(floor, place, row, name, author)
        elif choice == "2":
            place = input("Enter place: ")
            show_stats(place)
        elif choice == "3":
            name = input("Enter book name: ")
            delete_book(name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
