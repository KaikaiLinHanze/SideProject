"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH,  brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(window_width-paddle_width)/2
                            , y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        self.draw_bricks()
        self.__dx = 0
        self.__dy = 0
        self.get_dx()
        self.get_dy()
        self.touch_object()
        self.set_ball_position()
        self.touch_wall()
        self.brick_number = brick_cols * brick_rows
        onmousemoved(self.move)
        onmouseclicked(self.ball_velocity)

    def set_ball_position(self):
        # use to set ball to its original position
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0

    def touch_wall(self):
        # when touch wall the ball will bounce to the opposite side
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def touch_object(self):
        # if ball touch other objects will remove and bounce to the opposite side
        # if ball touch paddle will only bounce to the opposite side
        for i in range(0, self.ball.width+1, self.ball.width):
            for j in range(0, self.ball.height+1, self.ball.height):
                zone = self.window.get_object_at(self.ball.x + i, self.ball.y + j)
                if zone is not None and zone is not self.paddle:
                    self.window.remove(zone)
                    self.__dy = - self.__dy
                    self.brick_number -= 1
                    break
                if zone is not None and zone is self.paddle:
                    self.__dy = - self.__dy
                    dy = self.__dy
                    if dy > 0:
                        # use to avoid bouncing in the paddle
                        self.__dy = - self.__dy
                        break
                    else:
                        break

    def ball_velocity(self, event):
        # give velocity to the ball
        # Default initial velocity for the ball
        if self.ball.x == (self.window.width - self.ball.width) / 2 and \
                self.ball.y == (self.window.height - self.ball.height) / 2:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def get_dx(self):
        # getter dx
        return (self.__dx)

    def get_dy(self):
        # getter dy
        return (self.__dy)
        # Initialize our mouse listeners

    def move(self, catch_ball):
        # use to control paddle
        self.paddle.x = catch_ball.x - 1/2 * PADDLE_WIDTH
        self.paddle.y = self.window.height - PADDLE_OFFSET
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    def draw_bricks(self):
        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT)
                brick.filled = True
                brick.color = "white"
                if j <= 1:
                    brick.fill_color = "red"
                elif j <= 3:
                    brick.fill_color = "orange"
                elif j <= 5:
                    brick.fill_color = "yellow"
                elif j <= 7:
                    brick.fill_color = "green"
                else:
                    brick.fill_color = "blue"
                self.window.add(brick, x=i*(brick.width+BRICK_SPACING), y=j*(brick.height+BRICK_SPACING)+BRICK_OFFSET)



