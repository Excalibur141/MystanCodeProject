"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    x_coordinate = GRAPH_MARGIN_SIZE + year_index * (width-2*GRAPH_MARGIN_SIZE) / len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Vertical line & Year_index
    for i in range(len(YEARS)):
        # Vertical line
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        # Year_index
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW, font="arial 12")


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # py babygraphics.py
    # Kylie Nicholas Sonja
    # Jennifer Lucy
    # Kylie Nicholas Sonja Jennifer Lucy
    # ----- Write your code below this line ----- #

    # Dict -> name_data{name: {year: rank}}
    # List -> lookup_names[str1, str2, str3]
    for i in range(len(lookup_names)):  # lookup_names[i=0, i=1, i=2]
        for name, value in name_data.items():  # key = name, value = {year: rank}
            # Check if the name is in the list
            if lookup_names[i] == name:
                # Create the line , text and fill color
                previous_coordinate_x = GRAPH_MARGIN_SIZE
                previous_coordinate_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                # Color control -> 0,1,2,3,0,1,2,3....
                color_order = i % 4
                for j in range(len(YEARS)):
                    switch = True  # reset switch on : confirm that the ranking is 0 or other
                    for year, rank in name_data[lookup_names[i]].items():
                        if YEARS[j] == int(year):
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, (int(year) - YEARS[0]) / 10) + TEXT_DX,
                                               20 + float(rank) * 0.56,
                                               text=(lookup_names[i], rank),
                                               anchor=tkinter.SW,
                                               font="arial 12",
                                               fill=COLORS[color_order])
                            # Avoid drawing a vertical line at the beginning
                            if YEARS[0] != YEARS[j]:
                                canvas.create_line(previous_coordinate_x,
                                                   previous_coordinate_y,
                                                   get_x_coordinate(CANVAS_WIDTH, (int(year) - YEARS[0]) / 10),
                                                   20 + float(rank) * 0.56,
                                                   width=LINE_WIDTH,
                                                   fill=COLORS[color_order])
                            previous_coordinate_x = get_x_coordinate(CANVAS_WIDTH,
                                                                     (int(year) - YEARS[0]) / 10)
                            previous_coordinate_y = 20 + float(rank) * 0.56
                            switch = False  # switch off : avoid going to the "next part" (avoid double counting)
                    # I'm "next part"
                    if switch:  # if True(switch on):
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, (int(YEARS[j]) - YEARS[0]) / 10) + TEXT_DX,
                                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           text=(lookup_names[i], "*"),
                                           anchor=tkinter.SW,
                                           font="arial 12",
                                           fill=COLORS[color_order])
                        canvas.create_line(previous_coordinate_x,
                                           previous_coordinate_y,
                                           get_x_coordinate(CANVAS_WIDTH, (int(YEARS[j]) - YEARS[0]) / 10),
                                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH,
                                           fill=COLORS[color_order])
                        previous_coordinate_x = get_x_coordinate(CANVAS_WIDTH,
                                                                 (int(YEARS[j]) - YEARS[0]) / 10)
                        previous_coordinate_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
