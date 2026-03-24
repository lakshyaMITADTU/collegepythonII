# Dictionary example

def run_dict():
    student = {"id": 101, "name": "Aman", "marks": 85}
    print("Student:", student)

    # Access
    print("Name:", student["name"])
    print("Marks:", student.get("marks"))

    # Modify
    student["marks"] = 90
    student["grade"] = "A"
    print("Updated:", student)

    # Delete
    student.pop("id")
    print("After deletion:", student)

run_dict()
