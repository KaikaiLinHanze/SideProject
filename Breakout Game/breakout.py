"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 2000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts

def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        speed_x = graphics.get_dx()
        speed_y = graphics.get_dy()
        pause(FRAME_RATE)
        brick_remain = graphics.brick_number
        graphics.ball.move(dx=speed_x, dy=speed_y)
        graphics.touch_wall()
        graphics.touch_object()
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.set_ball_position()
        if brick_remain == 0 or lives == 0:
            break

    print("end game")








if __name__ == '__main__':
    main()
