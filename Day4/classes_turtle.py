from random import randint
import turtle
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x <self.x <rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distane_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
#
class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x)*(self.point2.y - self.point1.y)

class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        turtle.done()

gui_rectangle = GuiRectangle(Point(randint(0,100), randint(0,100)),
                             Point(randint(100, 200), randint(100, 200)))

myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)
print(gui_rectangle.area())