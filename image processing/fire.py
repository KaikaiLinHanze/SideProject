"""
File: fire.py
Name:Kai
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:str, the file path of the original image
    :return:The image with highlight fires
    """
    my_img = SimpleImage(filename)
    for x in range(my_img.width):
        for y in range(my_img.height):
            pixel_fire = my_img.get_pixel(x, y)
            avg = (pixel_fire.red + pixel_fire.green + pixel_fire.blue) // 3
            if pixel_fire.red > avg * HURDLE_FACTOR :
                pixel_fire.red = 255
                pixel_fire.green = 0
                pixel_fire.blue = 0
            else:
                pixel_fire.red = avg
                pixel_fire.green = avg
                pixel_fire.blue = avg
    return my_img


def main():
    """
    Using a function highlight_fires which detects the
    pixels that are recognized as fire
    and highlights them for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    # original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
