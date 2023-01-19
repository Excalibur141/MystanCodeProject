"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    ball = graphics.ball
    break_bricks = 0
    # Add the animation loop here!
    while True:
        # close game
        if lives == 0:
            graphics.window.add(graphics.game_over)
            break
        if break_bricks == graphics.total_bricks:
            graphics.window.add(graphics.game_win)
            break
        # restart
        if ball.y+ball.height > graphics.window.height:
            lives -= 1
            print("lives", lives)
            graphics.reset_ball()
        # update
        ball.move(graphics.get_dx(), graphics.get_dy())
        ball_upper_left = graphics.window.get_object_at(ball.x, ball.y)
        ball_upper_right = graphics.window.get_object_at(ball.x + ball.width, ball.y)
        ball_lower_left = graphics.window.get_object_at(ball.x, ball.y + ball.height)
        ball_lower_right = graphics.window.get_object_at(ball.x + ball.width, ball.y + ball.height)
        # check
        # check for collisions
        if ball_upper_left is not None:
            # paddle collision
            if ball_upper_left == graphics.paddle:
                graphics.set_dy(-graphics.get_dy())
            # bricks collision
            else:
                graphics.window.remove(ball_upper_left)
                graphics.set_dy(-graphics.get_dy())
                break_bricks += 1
        elif ball_upper_right is not None:
            if ball_upper_right == graphics.paddle:
                graphics.set_dy(-graphics.get_dy())
            else:
                graphics.window.remove(ball_upper_right)
                graphics.set_dy(-graphics.get_dy())
                break_bricks += 1
        elif ball_lower_left is not None:
            if ball_lower_left == graphics.paddle:
                graphics.set_dy(-graphics.get_dy())
            else:
                graphics.window.remove(ball_lower_left)
                graphics.set_dy(-graphics.get_dy())
                break_bricks += 1
        elif ball_lower_right is not None:
            if ball_lower_right == graphics.paddle:
                graphics.set_dy(-graphics.get_dy())
            else:
                graphics.window.remove(ball_lower_right)
                graphics.set_dy(-graphics.get_dy())
                break_bricks += 1
        # check for window boundary
        if ball.x <= 0 or ball.x+ball.width > graphics.window.width:
            graphics.set_dx(-graphics.get_dx())
        if ball.y <= 0:
            graphics.set_dy(-graphics.get_dy())
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
