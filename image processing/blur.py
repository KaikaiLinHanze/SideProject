"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage
BLUR = 5

def blur(img):
    """
    :param img: with its surround pixel average to its pixel
    :return: img with a blur pic
    """
    old_img = img
    new_img_blank = img.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            new_img_blank_pixel = new_img_blank.get_pixel(x,y)
            if (x,y) == (0, 0):
                new_img_blank_pixel.red = (old_img.get_pixel(0,0).red + old_img.get_pixel(0,1).red +
                                           old_img.get_pixel(1,1).red + old_img.get_pixel(1,0).red) / 4
                new_img_blank_pixel.green = (old_img.get_pixel(0,0).green + old_img.get_pixel(0,1).green +
                                             old_img.get_pixel(1,1).green + old_img.get_pixel(1,0).green ) / 4
                new_img_blank_pixel.blue = (old_img.get_pixel(0,0).blue + old_img.get_pixel(0,1).blue +
                                            old_img.get_pixel(1,1).blue + old_img.get_pixel(1,0).blue ) / 4
            if (x,y) == (old_img.width-1, 0):
                new_img_blank_pixel.red = (old_img.get_pixel(old_img.width-1,0).red +
                                           old_img.get_pixel(old_img.width-2,1).red +
                                           old_img.get_pixel(old_img.width-1,1).red +
                                           old_img.get_pixel(old_img.width-2,0).red) / 4
                new_img_blank_pixel.green = (old_img.get_pixel(old_img.width-1,0).green +
                                             old_img.get_pixel(old_img.width-2,1).green +
                                             old_img.get_pixel(old_img.width-1,1).green +
                                             old_img.get_pixel(old_img.width-2,0).green ) / 4
                new_img_blank_pixel.blue = (old_img.get_pixel(old_img.width-1,0).blue +
                                            old_img.get_pixel(old_img.width-2,1).blue +
                                            old_img.get_pixel(old_img.width-1,1).blue +
                                            old_img.get_pixel(old_img.width-2,0).blue) / 4
            if (x,y) == (old_img.width - 1, old_img.height - 1):
                new_img_blank_pixel.red = (old_img.get_pixel(old_img.width - 1, old_img.height - 1).red +
                                           old_img.get_pixel(old_img.width - 1, old_img.height - 2).red +
                                           old_img.get_pixel(old_img.width - 2, old_img.height - 1).red +
                                           old_img.get_pixel(old_img.width - 2, old_img.height - 2).red) / 4
                new_img_blank_pixel.green = (old_img.get_pixel(old_img.width - 1, old_img.height - 1).green +
                                             old_img.get_pixel(old_img.width - 1, old_img.height - 2).green +
                                             old_img.get_pixel(old_img.width - 2, old_img.height - 1).green +
                                             old_img.get_pixel(old_img.width - 2, old_img.height - 2).green) / 4
                new_img_blank_pixel.blue = (old_img.get_pixel(old_img.width - 1, old_img.height - 1).blue +
                                            old_img.get_pixel(old_img.width - 1, old_img.height - 2).blue +
                                            old_img.get_pixel(old_img.width - 2, old_img.height - 1).blue +
                                            old_img.get_pixel(old_img.width - 2, old_img.height - 2).blue) / 4
            if (x,y) == (0, old_img.height-1):
                new_img_blank_pixel.red = (old_img.get_pixel(0,old_img.height - 1).red +
                                           old_img.get_pixel(0,old_img.height - 2).red +
                                           old_img.get_pixel(1,old_img.height - 1).red +
                                           old_img.get_pixel(1,old_img.height - 2).red) / 4
                new_img_blank_pixel.green = (old_img.get_pixel(0,old_img.height - 1).green +
                                           old_img.get_pixel(0,old_img.height - 2).green +
                                           old_img.get_pixel(1,old_img.height - 1).green +
                                           old_img.get_pixel(1,old_img.height - 2).green) / 4
                new_img_blank_pixel.blue = (old_img.get_pixel(0,old_img.height - 1).blue +
                                           old_img.get_pixel(0,old_img.height - 2).blue +
                                           old_img.get_pixel(1,old_img.height - 1).blue +
                                           old_img.get_pixel(1,old_img.height - 2).blue) / 4
            if x > 0 and x < (old_img.width - 1) and y > 0 and y < (old_img.height - 1):
                new_img_blank_pixel.red = (old_img.get_pixel(x-1,y+1).red + old_img.get_pixel(x,y+1).red +
                                           old_img.get_pixel(x+1,y+1).red + old_img.get_pixel(x-1,y).red +
                                           old_img.get_pixel(x,y).red+ old_img.get_pixel(x+1,y).red +
                                           old_img.get_pixel(x-1,y-1).red+ old_img.get_pixel(x,y-1).red +
                                           old_img.get_pixel(x+1,y-1).red) / 9
                new_img_blank_pixel.green = (old_img.get_pixel(x-1,y+1).green + old_img.get_pixel(x,y+1).green +
                                             old_img.get_pixel(x+1,y+1).green + old_img.get_pixel(x-1,y).green +
                                             old_img.get_pixel(x,y).green + old_img.get_pixel(x+1,y).green +
                                             old_img.get_pixel(x-1,y-1).green + old_img.get_pixel(x,y-1).green +
                                             old_img.get_pixel(x+1,y-1).green) / 9
                new_img_blank_pixel.blue =(old_img.get_pixel(x-1,y+1).blue + old_img.get_pixel(x,y+1).blue +
                                           old_img.get_pixel(x+1,y+1).blue + old_img.get_pixel(x-1,y).blue +
                                           old_img.get_pixel(x,y).blue + old_img.get_pixel(x+1,y).blue +
                                           old_img.get_pixel(x-1,y-1).blue+ old_img.get_pixel(x,y-1).blue +
                                           old_img.get_pixel(x+1,y-1).blue) / 9
            if x > 0 and x < (old_img.width - 1) and y ==0:
                new_img_blank_pixel.red = (old_img.get_pixel(x-1, y).red + old_img.get_pixel(x, y).red +
                                           old_img.get_pixel(x+1, y).red + old_img.get_pixel(x-1, y+1).red +
                                           old_img.get_pixel(x, y+1).red + old_img.get_pixel(x+1, y+1).red) / 6
                new_img_blank_pixel.green = (old_img.get_pixel(x-1, y).green + old_img.get_pixel(x, y).green +
                                             old_img.get_pixel(x+1, y).green + old_img.get_pixel(x-1, y+1).green +
                                             old_img.get_pixel(x, y+1).green + old_img.get_pixel(x+1, y+1).green) / 6
                new_img_blank_pixel.blue = (old_img.get_pixel(x-1, y).blue + old_img.get_pixel(x, y).blue +
                                            old_img.get_pixel(x+1, y).blue + old_img.get_pixel(x-1, y+1).blue +
                                            old_img.get_pixel(x, y+1).blue + old_img.get_pixel(x+1, y+1).blue) / 6
            if x == 0 and y > 0 and y < (old_img.height - 1):
                new_img_blank_pixel.red = (old_img.get_pixel(x, y+1).red + old_img.get_pixel(x+1, y+1).red +
                                           old_img.get_pixel(x, y).red + old_img.get_pixel(x+1, y).red +
                                           old_img.get_pixel(x, y-1).red + old_img.get_pixel(x+1, y-1).red) / 6
                new_img_blank_pixel.green = (old_img.get_pixel(x, y+1).green + old_img.get_pixel(x+1, y+1).green +
                                           old_img.get_pixel(x, y).green + old_img.get_pixel(x+1, y).green +
                                           old_img.get_pixel(x, y-1).green + old_img.get_pixel(x+1, y-1).green) / 6
                new_img_blank_pixel.blue = (old_img.get_pixel(x, y+1).blue + old_img.get_pixel(x+1, y+1).blue +
                                           old_img.get_pixel(x, y).blue + old_img.get_pixel(x+1, y).blue +
                                           old_img.get_pixel(x, y-1).blue + old_img.get_pixel(x+1, y-1).blue) / 6
            if x == old_img.width - 1 and y > 0 and y < (old_img.height - 1):
                new_img_blank_pixel.red = (old_img.get_pixel(x-1, y+1).red + old_img.get_pixel(x, y+1).red +
                                           old_img.get_pixel(x, y).red + old_img.get_pixel(x-1, y).red +
                                           old_img.get_pixel(x, y-1).red + old_img.get_pixel(x-1, y-1).red) / 6
                new_img_blank_pixel.green = (old_img.get_pixel(x, y+1).green + old_img.get_pixel(x-1, y+1).green +
                                           old_img.get_pixel(x, y).green + old_img.get_pixel(x-1, y).green +
                                           old_img.get_pixel(x, y-1).green + old_img.get_pixel(x-1, y-1).green) / 6
                new_img_blank_pixel.blue = (old_img.get_pixel(x, y+1).blue + old_img.get_pixel(x-1, y+1).blue +
                                           old_img.get_pixel(x, y).blue + old_img.get_pixel(x-1, y).blue +
                                           old_img.get_pixel(x, y-1).blue + old_img.get_pixel(x-1, y-1).blue) / 6
            if x > 0 and x < (old_img.width - 1) and y ==(old_img.height - 1):
                new_img_blank_pixel.red = (old_img.get_pixel(x-1, y).red + old_img.get_pixel(x, y).red +
                                           old_img.get_pixel(x+1, y).red + old_img.get_pixel(x-1, y-1).red +
                                           old_img.get_pixel(x, y-1).red + old_img.get_pixel(x+1, y-1).red) / 6
                new_img_blank_pixel.green = (old_img.get_pixel(x-1, y).green + old_img.get_pixel(x, y).green +
                                             old_img.get_pixel(x+1, y).green + old_img.get_pixel(x-1, y-1).green +
                                             old_img.get_pixel(x, y-1).green + old_img.get_pixel(x+1, y-1).green) / 6
                new_img_blank_pixel.blue = (old_img.get_pixel(x-1, y).blue + old_img.get_pixel(x, y).blue +
                                            old_img.get_pixel(x+1, y).blue + old_img.get_pixel(x-1, y-1).blue +
                                            old_img.get_pixel(x, y-1).blue + old_img.get_pixel(x+1, y-1).blue) / 6
    return new_img_blank
def main():
    """
        The blur algorithm uses the average RGB values of a pixel's nearest neighbors.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(BLUR):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
