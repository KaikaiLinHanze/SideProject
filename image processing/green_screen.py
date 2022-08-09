"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
           fig_p = figure_img.get_pixel(x, y)
           back_p = background_img.get_pixel(x, y)
           bigger = max(fig_p.red, fig_p.blue)
           if fig_p.green > 2 * bigger:
               fig_p.red = back_p.red
               fig_p.blue = back_p.blue
               fig_p.green = back_p.green
    return figure_img

def main():
    """
    MillenniumFalcon.png as background and
    replace the green pixels in "ReyGreenScreen.png".
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.make_as_big_as(figure)
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
