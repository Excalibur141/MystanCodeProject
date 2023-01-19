"""
File: my_drawing
Name: Jhin
----------------------
1. create and define circle1
2. create and define circle2
3. create and define tri1
4. create and define tri2
5. create and define label1
6. create and define label2
7. create and define label3

"""

from campy.graphics.gobjects import GOval, GLabel, GPolygon
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(width=1000, height=500, title="LOL")


def main():
    """
    Title: Most addicting game
    This game accompanied me through the happiest time of my life
    """
    onmouseclicked(create_a_point)
    circle1 = GOval(300, 300, x=(window.width-300)/2, y=25)
    circle1.filled = True
    circle1.fill_color = "gold"
    window.add(circle1)

    circle2 = GOval(250, 250, x=(window.width-250)/2, y=50)
    circle2.filled = True
    circle2.fill_color = "navy"
    window.add(circle2)

    tri = GPolygon()
    tri.add_vertex((375, 5))
    tri.add_vertex((450, 5))
    tri.add_vertex((450, 285))
    tri.add_vertex((650, 285))
    tri.add_vertex((600, 325))
    tri.add_vertex((375, 325))
    tri.add_vertex((400, 285))
    tri.add_vertex((400, 40))
    tri.add_vertex((375, 5))
    tri.filled = True
    tri.fill_color = "gold"
    window.add(tri)

    tri2 = GPolygon()
    tri2.add_vertex((400, 40))
    tri2.add_vertex((400, 285))
    tri2.add_vertex((425, 245))
    tri2.add_vertex((425, 75))
    tri2.filled = True
    tri2.fill_color = "goldenrod"
    window.add(tri2)

    label1 = GLabel("LEAGUE", 325, 400)
    label1.font = '-50'
    window.add(label1)

    label2 = GLabel("of", 590, 390)
    label2.font = '-20'
    window.add(label2)

    label3 = GLabel("LEGENDS", 300, 475)
    label3.font = '-60'
    window.add(label3)


def create_a_point(mouse):
    circle = GOval(1, 1, x=mouse.x - 1 / 2, y=mouse.y - 1 / 2)
    print(circle)
    window.add(circle)


if __name__ == '__main__':
    main()
