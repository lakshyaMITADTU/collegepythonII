import pickle as p

# -------- WRITE DATA --------
def write_data():
    student = {
        "name": input("Enter name: "),
        "marks": int(input("Enter marks: "))
    }

    with open("student.dat", "wb") as f:
        p.dump(student, f)

    print("Student data stored successfully")


# -------- READ DATA --------
def read_data():
    try:
        with open("student.dat", "rb") as f:
            data = p.load(f)
            print("Student Data:", data)
    except:
        print("File not found")


# -------- STORE IMAGE --------
def store_image():
    try:
        with open("image.jpeg", "rb") as img:
            data = img.read()

        with open("image.dat", "wb") as f:
            p.dump(data, f)

        print("Image stored successfully")
    except:
        print("Image file not found")


# -------- MENU --------
while True:
    print("\n--- PICKLE MENU ---")
    print("1. Write Student Data")
    print("2. Read Student Data")
    print("3. Store Image")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        write_data()
    elif choice == 2:
        read_data()
    elif choice == 3:
        store_image()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
