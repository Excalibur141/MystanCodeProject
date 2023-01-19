"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
# constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
# attribute


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window.width - paddle_width) / 2, y=(self.window.height - paddle_offset))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius,
                          x=(self.window.width-2*ball_radius)/2, y=(self.window.height-2*ball_radius)/2)
        self.x_starter = self.ball.x
        self.y_starter = self.ball.y
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.action)
        onmousemoved(self.set_paddle_position)
        self.lives = 3

        # Draw bricks # class calling object (function)
        self.draw_bricks(self, brick_cols, brick_rows, brick_width, brick_height, brick_spacing)
        self.total_bricks = brick_rows * brick_cols

        # Label
        self.game_over = GLabel("Game Over", x=self.paddle.x, y=self.paddle.y)
        self.game_over.font = '-40'
        self.game_win = GLabel("You win!!", x=self.paddle.x, y=self.paddle.y)
        self.game_win.font = '-40'

    # Ball animation
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):  # like assign a variable from coder to user
        return self.__dx

    def get_dy(self):
        return self.__dy

    # tip:need to define a variable in ( , ) to catch value on user
    def set_dx(self, dx):  # like a box to catch variable on user
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def action(self, mouse):  # the switch is given velocity
        if self.__dx == 0 and self.__dy == 0:
            self.set_ball_velocity()

    def set_ball_position(self):  # let ball stay at middle of the window
        self.ball.x = self.x_starter
        self.ball.y = self.y_starter

    def reset_ball(self):  # let ball stay at middle of the window and stop the move of the ball
        self.set_ball_position()
        self.__dx = 0
        self.__dy = 0

    # Paddle animation
    def set_paddle_position(self, mouse):
        # because mouse need to center the paddle, it will need to deduct half of the width (self.paddle.width/2)
        if mouse.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    @staticmethod
    def draw_bricks(self, brick_cols, brick_rows, brick_width, brick_height, brick_spacing):
        for i in range(brick_cols):  # create bricks using the rocket building concept (SC001)
            for j in range(brick_rows):
                # i=0, j=0,1
                # i=1, j=0,1
                # i=3, j=...
                self.brick = GRect(brick_width, brick_height,
                                   x=0+(brick_width + brick_spacing)*i, y=0+(brick_height + brick_spacing)*j)
                self.brick.filled = True
                if j == 0 or j == 1:  # change color every two rows
                    self.brick.fill_color = "red"
                    self.brick.color = "red"
                if j == 2 or j == 3:
                    self.brick.fill_color = "orange"
                    self.brick.color = "orange"
                if j == 4 or j == 5:
                    self.brick.fill_color = "yellow"
                    self.brick.color = "yellow"
                if j == 6 or j == 7:
                    self.brick.fill_color = "green"
                    self.brick.color = "green"
                if j == 8 or j == 9:
                    self.brick.fill_color = "blue"
                    self.brick.color = "blue"
                self.window.add(self.brick)
