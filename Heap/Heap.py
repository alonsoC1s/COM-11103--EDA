class Heap:
    def __init__(self):
        self.values = []
        self.values.append(None)

    def push(self, value):
        self.values.append(value)
        idx = len(self.values) - 1
        while idx > 1 and value < self.values[idx >> 1]:
            self.values[idx] = self.values[idx >> 1]
            idx >>= 1
            self.values[idx] = value

    def insert(self, *args):
        for x in args:
            self.push(x)

    def peek(self):
        return self.values[1]

    def pop(self):
        if len(self.values) <= 2:
            return self.values.pop()

        res = self.values[1]
        self.values[1] = self.values.pop()
        value = self.values[1]
        idx = 1
        fixed = False
        while fixed is False:
            if (idx << 1) + 1 < len(self.values):
                if self.values[idx << 1] < value and self.values[(idx << 1) + 1] < value:
                    fixed = True
                else:
                    if self.values[idx << 1] < self.values[(idx << 1) + 1]:
                        self.values[idx] = self.values[idx << 1]
                        idx = idx << 1
                    else:
                        self.values[idx] = self.values[(idx << 1) + 1]
                        idx = (idx << 1) + 1
            else:
                if idx << 1 < len(self.values) and self.values[idx << 1] < value:
                    self.values[idx] = self.values[idx << 1]
                    idx = idx << 1
                else:
                    fixed = True
            self.values[idx] = value
        return res

    def isEmpty(self):
        if len(self.values) <= 1:
            return True
        else:
            return False


monti = Heap()
monti.insert(-2, 3, 2, 1, 0)
while monti.isEmpty() is False:
    print(monti.pop())