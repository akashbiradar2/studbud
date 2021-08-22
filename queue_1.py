# implement an que using array
class arrayquequ:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def lenght(self):
        return self.size

    def isempty(self):
        return self.size == 0
    def enquequ(self,x):
        self.data.append(x)
        self.size = self.size + 1
    def dequequ(self):
        if self.isempty():
            return
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front + 1
        self.size = self.size - 1
        return value
    def first(self):
        if self.isempty():
            return
        return self.data[self.front]
    def print(self):
        for i in range(len(self.data)):
            print(self.data[i])

q = arrayquequ()
q.enquequ(5)
q.enquequ(6)
q.enquequ(8)
q.dequequ()
q.enquequ(5)
q.print()
print(q.first())