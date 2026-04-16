class Stack:
    def __init__(self):
        self.stack = []   # initialize empty stack

    def push(self, element):
        self.stack.append(element)
        print("Pushed:", element)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Popped:", self.stack.pop())

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        print("Stack:", self.stack)


# main program
s = Stack()

while True:
    print("\n1.Push 2.Pop 3.Peek 4.Display 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        s.push(val)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
