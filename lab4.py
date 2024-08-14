#lec question----------------------------------

""" class Shape:

    def __init__(self):
    
        self._area = 0
        self._perimeter = 0

    def area(self):
        print("Area of the shape: ", self._area)

    def perimeter(self):
        print("Perimeter of the shape: ", self._perimeter)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self._length = length

    def area(self):
        self._area = self._length ** 2
        super().area()

    def perimeter(self):
        self._perimeter = 4 * self._length
        super().perimeter()

s = Square(5)
s.area()
s.perimeter()  """ 


#lab questions----------------------------------
#question 1-------------------------------------



class Queue:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)

    def is_empty(self):
        return len(self.values) == 0

    def pop(self):
        if not self.is_empty():
            return self.values.pop(0)
        else:
            print("Warning: trying to pop from an empty queue")
            return None

    
    def print_queue(self):
        print(self.values)
    

q = Queue()

print(q.is_empty())
q.insert(1)
q.insert(2)
q.insert(3)
q.print_queue() 

print(q.is_empty())
print(q.pop()) 
q.print_queue() 

#-----------------------------------------


class NameableQueue(Queue):
    queues = {}

    def __init__(self, name, max_size):
        super().__init__()
        self.name = name
        self.max_size = max_size
        NameableQueue.queues[name] = self

    def insert(self, value):
        if len(self.values) < self.max_size:
            super().insert(value)
        else:
            raise QueueOutOfRangeException(f"Queue {self.name} is full.")

    @classmethod
    def save(cls, filename):
        with open(filename, 'w') as f:
            for name, queue in cls.queues.items():
                f.write(f"{name}={str(queue.values)}\n")

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                name, values = line.strip().split('=')
                queue = NameableQueue(name, 0)
                queue.values = eval(values)
                NameableQueue.queues[name] = queue

class QueueOutOfRangeException(Exception):
    pass                

q1 = NameableQueue("queue1", 3)
q1.insert(1)
q1.insert(2)
q1.insert(3)

try:
    q1.insert(4)
except QueueOutOfRangeException as e:
    print(e)  

NameableQueue.save("file2.txt")


NameableQueue.load("file2.txt")

print(q1.pop())  
print(q1.pop())  
print(q1.pop())  
print(q1.is_empty()) 
print(NameableQueue.queues.keys())  


q2 = NameableQueue("queue2", 4)
q2.insert(1)
q2.insert(2)
q2.insert(3)

try:
    q2.insert(4)
except QueueOutOfRangeException as e:
    print(e)  

NameableQueue.save("file2.txt")


NameableQueue.load("file2.txt")
print(NameableQueue.queues)

print(NameableQueue.queues.keys())  


