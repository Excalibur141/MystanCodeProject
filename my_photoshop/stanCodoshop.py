"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
# py stanCodoshop.py hoover


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.
    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    #
    red_avg = red
    green_avg = green
    blue_avg = blue
    color_distance = ((red_avg - pixel.red)**2 + (green_avg - pixel.green)**2 + (blue_avg - pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.
    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # pixels(list) = [pixel_0, pixel_1, pixel_2]
    # pixels(list) = [[red_0, green_0, blue_0], [red_1, green_1, blue_1], [red_2, green_2, blue_2]]
    # return rgb(list) = [avg_red, avg_green, avg_blue]

    rgb = []
    # total = 0
    # for i in range(len(pixels)):
    #     total +=
    total_red = 0
    total_green = 0
    total_blue = 0
    for i in range(len(pixels)):
        total_red += pixels[i].red
    for i in range(len(pixels)):
        total_green += pixels[i].green
    for i in range(len(pixels)):
        total_blue += pixels[i].blue
    avg_red = total_red // len(pixels)  # because we need the answer to be an integer -> "//"
    avg_green = total_green // len(pixels)
    avg_blue = total_blue // len(pixels)
    rgb.append(avg_red)
    rgb.append(avg_green)
    rgb.append(avg_blue)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # pixels(list) = [pixel_0, pixel_1, pixel_2]
    # pixels(list) = [[red_0, green_0, blue_0], [red_1, green_1, blue_1], [red_2, green_2, blue_2]]
    # distance_list = [distance_0, distance_1, distance_2]
    # return best(Pixel)
    best = []
    distance_list = []
    avg_point = get_average(pixels)
    for i in range(len(pixels)):
        color_distance = get_pixel_dist(pixels[i], avg_point[0], avg_point[1], avg_point[2])
        distance_list.append(color_distance)
    # print(distance_list)  # only for test
    for i in range(1, len(pixels)):  # i = 1, 2
        if distance_list[i-1] <= distance_list[i]:  # (0, 1), (1, 2)
            best.append(pixels[i-1])
        else:  # if the last one is closest
            best.append(pixels[i])
    return best[0]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # # Milestone1
    # green_im = SimpleImage.blank(20, 20, "green")
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # # Milestone2
    # green_pixel = SimpleImage.blank(20, 20, "green").get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, "red").get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, "blue").get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # # Milestone3
    # green_pixel = SimpleImage.blank(20, 20, "green").get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, "red").get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, "blue").get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # Milestone4
    """
    images = [image_1, image_2, image_3, image_4]
    1. find the same coordinates at different images
    2. compare to select the best pixel
    3. put the best pixel to the result_image
    4. output result_image
    
    py stanCodoshop.py clock-tower
    py stanCodoshop.py hoover
    py stanCodoshop.py math-corner
    py stanCodoshop.py monster
    """
    pixels_to_compare = []  # put pixels on the list with the same coordinates
    for x in range(width):  # coordinate X
        for y in range(height):  # coordinate y
            for i in range(len(images)):  # for each image
                images_pixel = images[i].get_pixel(x, y)
                pixels_to_compare.append(images_pixel)
                # after putting all the pixels on the list, compare the pixels at the same coordinates
                if i == len(images)-1:
                    result_pixel = result.get_pixel(x, y)
                    best = get_best_pixel(pixels_to_compare)
                    result_pixel.red = best.red
                    result_pixel.green = best.green
                    result_pixel.blue = best.blue
                    pixels_to_compare = []  # reset the list
        progress = x / width
        print("progress", round(progress*100, 2), "%")  # let user track progress

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    # images(list) = [image1, image2, image3]
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
