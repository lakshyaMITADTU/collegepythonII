# Polymorphism example

class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

class Square(Shape):
    def draw(self):
        print("Drawing square")

items = [Circle(), Square()]

for obj in items:
    obj.draw()
