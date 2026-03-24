# Simple Library system

class BookStore:
    def __init__(self):
        self.store = ["Math", "Physics", "Python"]

    def display(self):
        print("Books:", self.store)

    def borrow(self, name):
        if name in self.store:
            self.store.remove(name)
            print("Borrowed:", name)
        else:
            print("Not found")

    def give_back(self, name):
        self.store.append(name)
        print("Returned:", name)


obj = BookStore()
obj.display()
obj.borrow("Math")
obj.display()
obj.give_back("Math")
