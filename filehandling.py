def write_file():
    f = open("sample.txt", "w")
    data = input("Enter text to write: ")
    f.write(data)
    f.close()
    print("Data written successfully")

def read_file():
    try:
        f = open("sample.txt", "r")
        print("\nFile Content:")
        print(f.read())
        f.close()
    except:
        print("File not found")

def append_file():
    f = open("sample.txt", "a")
    data = input("Enter text to append: ")
    f.write("\n" + data)
    f.close()
    print("Data appended successfully")

def count_words():
    try:
        f = open("sample.txt", "r")
        data = f.read()
        words = data.split()
        print("Total words:", len(words))
        f.close()
    except:
        print("File not found")


while True:
    print("\n--- FILE HANDLING MENU ---")
    print("1. Write File")
    print("2. Read File")
    print("3. Append File")
    print("4. Count Words")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        write_file()
    elif choice == 2:
        read_file()
    elif choice == 3:
        append_file()
    elif choice == 4:
        count_words()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
