# Working with Lists

def run_list():
    data = [5, 15, 25, 35, 45]
    print("List =", data)

    # Access
    print("First element:", data[0])
    print("Last element:", data[-1])
    print("Middle slice:", data[1:3])

    # Insert & append
    data.insert(1, 10)
    data.append(55)
    print("After insert & append:", data)

    # Delete
    data.pop(2)
    print("After pop:", data)

    if 35 in data:
        data.remove(35)

    # Sort
    print("Sorted:", sorted(data))
    print("Reverse sorted:", sorted(data, reverse=True))

run_list()
