class Queue:
    def __init__(self):
        self.queue = []  

    def enqueue(self, element):
        self.queue.append(element)
        print("Inserted:", element)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Removed:", self.queue.pop(0))

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        print("Queue:", self.queue)


# main program
q = Queue()

while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        q.enqueue(val)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
