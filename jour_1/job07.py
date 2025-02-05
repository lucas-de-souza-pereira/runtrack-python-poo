class Character:

    def __init__(self):

        self.x = 0
        self.y = 0


    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def top(self):
        self.y -= 1

    def bottom(self):
        self.y += 1

    def printPosition(self):
        return f"actual position ({self.x},{self.y})"

p1 = Character()

p1.left()
p1.right()
p1.right()
p1.right()
p1.right()
p1.top()
p1.top()
p1.bottom()
print(p1.printPosition())
