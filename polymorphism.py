class Shape:
    def draw(self):
        print("Drawing a shape")

class Parallelogram(Shape):
    def draw(self):
        print("Drawing a parallelogram")

class Rhombus:
    def draw(self):
        print("Drawing a Rhombus")


sh = Shape()
sh.draw()
p = Parallelogram()
p.draw()

r = Rhombus()
r.draw()
