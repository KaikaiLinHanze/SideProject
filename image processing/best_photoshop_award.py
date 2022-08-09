"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def main():
    """
    tomb.jpg as background and
    replace the green pixels in "finger.jpg".
    透過模仿薩諾斯彈手指的方式在導致宇宙毀滅，背景以墓園帶出
    """
    tomb = SimpleImage("image_contest/tomb.jpg")
    finger = SimpleImage("image_contest/finger.jpg")
    tomb.make_as_big_as(finger)
    result = combine(tomb, finger)
    result.show()

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
           if fig_p.green > 1.25 * bigger:
               fig_p.red = back_p.red
               fig_p.blue = back_p.blue
               fig_p.green = back_p.green
    return figure_img


if __name__ == '__main__':
    main()
