#################################################################
# FILE : image_editor.py
# WRITER : elhanan haenel 
# EXERCISE : intro2cs ex5 2022-2023
# DESCRIPTION: A simple program that do manipulation on image.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex5_helper import *
from typing import Optional
import sys


##############################################################################
#                                  Functions                                 #
##############################################################################

def is_float(s):
    '''Checks if a string can be casted to an integer'''
    try:
        float(s)
        return True
    except ValueError:
        return False


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """this function get a colored image and return a singel channel image"""
    channels = []
    for i in range(len(image)):
        b = []
        for j in range(len(image[i][0])):
            a = []
            for h in range(len(image[i])):
                a.append(image[i][h][j])
            b.append(a)
        channels.append(b)

    result = []
    for i in range(len(channels[0])):
        a = []
        for j in range(len(channels)):
            a.append(channels[j][i])
        result.append(a)
    return result


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    """this function get a singel channel image and return a singel channel
    image"""
    image = []
    for i in range(len(channels[0])):
        b = []
        for j in range(len(channels[0][0])):
            a = []
            for h in range(len(channels)):
                a.append(channels[h][i][j])
            b.append(a)
        image.append((b))
    return image


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """this function get a colored image and return a singel channel image"""
    SingleChannelImage = []
    for i in range(len(colored_image)):
        b = []
        for j in range(len(colored_image[i])):
            a = colored_image[i][j][0] * 0.299 + colored_image[i][j][
                1] * 0.587 + colored_image[i][j][2] * 0.114
            b.append(round(a))
        SingleChannelImage.append(b)
    return SingleChannelImage


def blur_kernel(size: int) -> Kernel:
    """this function get a size of kernel and return a list of the kernel"""
    kernel = []
    for i in range(size):
        a = []
        for j in range(size):
            a.append(1 / (size * size))
        kernel.append(a)
    return kernel


def calculte(matrix, kernel):
    """this function get a matriza and kernel, and return the sum of there
    multiplication"""
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # print(type(kernel[i][j]))
            # print(kernel)
            sum += matrix[i][j] * kernel[i][j]
    if sum > 255:
        sum = 255
    if sum < 0:
        sum = 0
    return round(sum)


def builde_box(image, i, j, size):
    """the function get a image and a location in the image, and return a
    matriza of the image based on a size that was given"""

    base_x = j - size // 2
    base_y = i - size // 2
    x_image = len(image[0]) - 1
    y_image = len(image) - 1
    colome = []
    for a in range(size):
        row = []
        for b in range(size):
            if base_x + b < 0 or base_y + a < 0 or \
                    base_x + b > x_image or base_y + a > y_image:
                row.append(image[i][j])
            else:
                row.append(image[base_y + a][base_x + b])
        colome.append(row)
    return colome


def apply_kernel(image: SingleChannelImage,
                 kernel: Kernel) -> SingleChannelImage:
    """the function get a image and a kernel and return a singel channle
    image"""
    row = []
    for i in range(len(image)):
        colume = []
        for j in range(len(image[i])):
            a = builde_box(image, i, j, len(kernel))
            colume.append(calculte(a, kernel))
        row.append(colume)
    SingleChannelImage = row
    return SingleChannelImage

    ...


def bilinear_interpolation(image: SingleChannelImage, y: float,
                           x: float) -> int:
    """this function get a image and corinate and return reisize of ceratin
    pixcel"""
    if int(x) == len(image[0]) - 1 and int(y) == len(image) - 1:
        sum = image[int(y)][int(x)]
    elif int(x) == len(image[0]) - 1:
        sum = image[int(y)][int(x)] * (1 + int(x) - x) * (1 + int(y) - y) + \
              image[int(y) + 1][int(x)] * (y - int(y)) * (1 + int(x) - x) + \
              0 + 0
    elif int(y) == len(image) - 1:
        # print(image[int(y)][int(x)])
        # print(1 + int(x) - x)
        sum = image[int(y)][int(x)] * (1 + int(x) - x) * (1 + int(y) - y) + \
              0 + \
              image[int(y)][int(x) + 1] * (x - int(x)) * (1 + int(y) - y) + 0
    else:
        # print(image[int(y)][int(x)])
        sum = image[int(y)][int(x)] * (1 + int(x) - x) * (1 + int(y) - y) + \
              image[int(y) + 1][int(x)] * (y - int(y)) * (1 + int(x) - x) + \
              image[int(y)][int(x) + 1] * (x - int(x)) * (1 + int(y) - y) + \
              image[int(y) + 1][int(x) + 1] * (x - int(x)) * (y - int(y))
    return round(sum)


def resize(image: SingleChannelImage, new_height: int,
           new_width: int) -> SingleChannelImage:
    """this function get a image and corinate and return reisize of image"""
    s = []
    size_x = (len(image[0]) - 1) / (new_width - 1)
    size_y = (len(image) - 1) / (new_height - 1)
    for i in range(new_height):
        a = []
        for j in range(new_width):
            send_x = size_x * j
            send_y = size_y * i
            a.append(bilinear_interpolation(image, send_y, send_x))
        s.append(a)
    return (s)
    ...


def rotate_90(image: Image, direction: str) -> Image:
    """the function get a image and direction, and return the image rotate
    to that direction"""
    a = []
    for i in range(len(image[0])):
        s = []
        for j in range(len(image) - 1, -1, -1):
            s.append(image[j][i])
        a.append(s)
    if direction == "L":
        s = []
        for i in a:
            s.append(i[::-1])
        a = s[::-1]
    return a

    ...


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int,
              c: float) -> SingleChannelImage:
    """the function get a image blur size, block size and 'c' and return the
    edge of the image"""
    image_blur = apply_kernel(image, blur_kernel(blur_size))
    image = image_blur
    # print(image)
    block_size_list = blur_kernel(block_size)
    row = []
    for i in range(len(image_blur)):
        colome = []
        for j in range(len(image_blur[i])):
            a = builde_box(image, i, j, block_size)
            sum = 0
            for h in a:
                for d in h:
                    sum += d
            sum = sum / (block_size ** 2)
            if image[i][j] < sum - c:
                colome.append(0)
            else:
                colome.append(255)
        row.append(colome)
    # print(row)
    return row

    ...


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    """"the function get a image and a number return a quzntize of the image
    base on the number given but on balck and white image"""
    row = []
    for i in range(len(image)):
        colome = []
        for j in range(len(image[i])):
            # print(image[i][j])
            colome.append(
                round(int((image[i][j] * (N / 256))) * (255 / (N - 1))))
        row.append(colome)
    return row


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    """"the function get a image and a number return a quzntize of the image
    base on the number given on colored image"""
    seperat_colors = separate_channels(image)
    a = []
    for i in range(len(seperat_colors)):
        a.append(quantize(seperat_colors[i], N))
    new_image = combine_channels(a)
    return new_image
    ...


def choice1(image, gray):
    """the function get a image and if the image is gray and return a gray
    image"""
    if gray:
        print("the image is allredy gray")
        return image, gray
    else:
        image = RGB2grayscale(image)
        gray = True
    return image, gray


def choice2(image, gray):
    """the function get a image and return the a blur image"""
    kernel = input("what kernel you want?")
    if is_float(kernel) != True:
        print("error, worng arguments")
        return image
    if float(kernel) % 2 != 1 or float(kernel) < 0 or "." in kernel:
        print("error, worng arguments")
        return image
    kernel = int(float(kernel))
    if gray:
        image = apply_kernel(image, blur_kernel(kernel))
    else:
        seperate_colors = separate_channels(image)
        a = []
        for i in range(len(seperate_colors)):
            a.append(apply_kernel(seperate_colors[i], blur_kernel(kernel)))
        image = combine_channels(a)
    return image


def choice3(image, gray):
    """the function get a image and return a resize image"""
    size = input("what size you want?")
    count = 0
    for i in size:
        if i == ",":
            count += 1
    if count != 1:
        print("error, worng arguments")
        return image
    size = size.split(",")
    if is_float(size[0]) != True or is_float(size[1]) != True:
        print("error, worng arguments")
        return image
    if "." in size[0] or "." in size[1]:
        print("error, worng arguments")
        return image
    row = int(float(size[0]))
    colome = int(float(size[1]))
    if row < 2 or colome < 2:
        print("error")
        return image
    if gray == False:
        seperat_colors = separate_channels(image)
        a = []
        for i in range(len(seperat_colors)):
            a.append(resize(seperat_colors[i], row, colome))
        new_image = combine_channels(a)
    else:
        new_image = resize(image, row, colome)
    return new_image


def choice4(image):
    """the function get a image and return a rotate image"""
    direction = input("what direction? L\\R")
    if direction != "L" and direction != "R":
        print("error, worng arguments")
        return image
    image = rotate_90(image, direction)
    return image


def choice5(image, gray):
    """the function get a image and return a edge photho of the image"""
    inputs = input("what blur size and block size and c:")
    count = 0
    for i in inputs:
        if i == ",":
            count += 1
    if count != 2:
        print("error, worng arguments")
        return image, gray
    inputs = inputs.split(",")
    for i in inputs:
        if is_float(i) != True:
            print("error, worng arguments")
            return image, gray
    if "." in inputs[0] or "." in inputs[1]:
        print("error, worng arguments")
        return image, gray
    blur_size, block_size, c = int(float(inputs[0])), int(
        float(inputs[1])), float(inputs[2])
    if blur_size % 2 == 0 or block_size % 2 == 0 or block_size < 0 or \
            block_size < 0 or c < 0:
        print("error, worng arguments")
        return image, gray
    if gray == False:
        image, gray = choice1(image, gray)
    image = get_edges(image, blur_size, block_size, c)
    return image, gray


def choice6(image, gray):
    """the function get a image and return a quantize image"""
    N = input("what number you want?")
    if is_float(N) != True:
        print("error, worng arguments")
        return image
    if int(float(N)) < 2 or "." in N:
        print("error, worng arguments")
        return image
    N = int(float(N))
    if gray:
        image = quantize(image, N)
    else:
        image = quantize_colored_image(image, N)
    return image


def get_path():
    """the function get the path from sys.argv and check if its valis"""
    n = len(sys.argv)
    # print(n)
    if n != 2:
        print("error!!!")
        exit()
    return sys.argv[1]


if __name__ == '__main__':
    """this is the main function"""
    path = get_path()
    image = load_image(path)

    stop = False
    gray = False
    messege = "Choice:\n\n 1 - convert to gray \n 2 - buler image\n 3 " \
              "- resize\n 4 - turn the image\n 5 - convert to edge photo\n 6 " \
              "" \
              "" \
              "" \
              "- " \
              "quantize the image\n 7 - show image\n 8 - exit\n\nYour choice " \
              "" \
              "" \
              "is?"
    while stop == False:
        messege_send = messege
        input_user = input(messege_send)
        messege_send = "error!!! wrong input\n" + messege
        while input_user not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            input_user = input(messege_send)
        if input_user == "1":
            image, gray = choice1(image, gray)
        elif input_user == "2":
            image = choice2(image, gray)
        elif input_user == "3":
            image = choice3(image,gray)
        elif input_user == "4":
            image = choice4(image)
        elif input_user == "5":
            image, gray = choice5(image, gray)
        elif input_user == "6":
            image = choice6(image, gray)
        elif input_user == "7":
            show_image(image)
        elif input_user == "8":
            stop = True
    address = input("what adrees you want to save the image?")
    save_image(image, address)
