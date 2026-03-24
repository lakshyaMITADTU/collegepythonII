# Inheritance demo

class Human:
    def __init__(self, n):
        self.n = n

    def show(self):
        print("Name:", self.n)


class Worker(Human):
    def __init__(self, n, sal):
        super().__init__(n)
        self.sal = sal

    def details(self):
        self.show()
        print("Salary:", self.sal)


w = Worker("Rohit", 40000)
w.details()
