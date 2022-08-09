"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(img):
    """
    :param img: with its surround pixel average to its pixel
    :return :img with a shrink pic
    """
    old_img = SimpleImage(img)
    new_img_blank = SimpleImage(img).blank((old_img.width//2), (old_img.height//2))
    for x in range(old_img.width):
        for y in range(old_img.height):
            new_img_blank_pixel = new_img_blank.get_pixel(x//2,y//2)
            if (x,y) == (0, 0):
                new_img_blank_pixel.red = (old_img.get_pixel(0,0).red + old_img.get_pixel(0,1).red +
                                           old_img.get_pixel(1,1).red + old_img.get_pixel(1,0).red) / 4
                new_img_blank_pixel.green = (old_img.get_pixel(0,0).green + old_img.get_pixel(0,1).green +
                                             old_img.get_pixel(1,1).green + old_img.get_pixel(1,0).green) / 4
                new_img_blank_pixel.blue = (old_img.get_pixel(0,0).blue + old_img.get_pixel(0,1).blue +
                                            old_img.get_pixel(1,1).blue + old_img.get_pixel(1,0).blue) / 4
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
    to shrink pic into 1/4 of its original size.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()
if __name__ == '__main__':
    main()
