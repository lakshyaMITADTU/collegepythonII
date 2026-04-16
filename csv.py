import csv

def write():
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["roll no.", "name", "marks"])

        while True:
            roll = int(input("Enter roll no: "))
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))

            writer.writerow([roll, name, marks])

            ch = input("More? (y/n): ")
            if ch.lower() == "n":
                break

    print("Data written successfully")


def count():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        count = 0
        for row in reader:
            count += 1

        print("Total records:", count)


write()
count()
