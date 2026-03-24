# Tuple usage

def run_tuple():
    t1 = (1, 2, 3, 4, 5)
    print("Tuple values:", t1)

    # Access
    print("Index 2:", t1[2])
    print("Slice:", t1[:3])

    # Nested
    combo = ("Code", (7, 8), ["x", "y"])
    print("Nested tuple:", combo)

    print("From inner tuple:", combo[1][0])
    print("From list:", combo[2][1])

    # Repeat
    t2 = ("A",)
    print("Repeated tuple:", t2 * 4)

run_tuple()
