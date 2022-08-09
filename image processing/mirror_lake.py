"""
File: mirror_lake.py
Name:Kai
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str, the file path of the original image
    :return:The image with reflect lake
    """
    my_img = SimpleImage(filename)
    my_img_blank = SimpleImage(filename).blank(my_img.width, my_img.height * 2)
    for x in range(my_img.width):
        for y in range(my_img.height):
            img_pixel = my_img.get_pixel(x, y)
            img_blank_pixel_p1 = my_img_blank.get_pixel(x, y)
            img_blank_pixel_p1.red = img_pixel.red
            img_blank_pixel_p1.green = img_pixel.green
            img_blank_pixel_p1.blue = img_pixel.blue

            img_blank_pixel_p2 = my_img_blank.get_pixel(x, 2 * my_img.height - 1 - y)
            img_blank_pixel_p2.red = img_pixel.red
            img_blank_pixel_p2.green = img_pixel.green
            img_blank_pixel_p2.blue = img_pixel.blue

    return my_img_blank


def main():
    """
    makes a new image that creates a mirror
    lake vibe by placing an inverse image of
    mt-rainier.jpg below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    # original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
