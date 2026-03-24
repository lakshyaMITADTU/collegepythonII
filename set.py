# Set operations demo

def run_sets():
    A = {10, 20, 30, 40}
    B = {30, 40, 50, 60}

    print("A:", A)
    print("B:", B)

    # Loop
    print("Elements of A:")
    for i in A:
        print(i)

    # Check
    print("20 exists in A?", 20 in A)

    # Operations
    print("A union B:", A.union(B))
    print("Common elements:", A.intersection(B))
    print("A - B:", A.difference(B))
    print("B - A:", B.difference(A))

run_sets()
