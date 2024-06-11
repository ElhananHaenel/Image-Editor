# Image Editor

## Introduction
This project is a simple image editor that allows users to perform various manipulations on images such as converting to grayscale, blurring, resizing, rotating, edge detection, and quantization. The image editor is implemented in Python and leverages basic image processing techniques.

## Project Details

### File Information
- **File**: `image_editor.py`
- **Author**: Elhanan Haenel
- **Exercise**: Introduction to Computer Science, Exercise 5, 2022-2023
- **Description**: A simple program for manipulating images.
- **Notes**: ...

### Functionality
The program includes the following main functions:
1. **Convert to Grayscale**
2. **Blur Image**
3. **Resize Image**
4. **Rotate Image**
5. **Edge Detection**
6. **Quantize Image**
7. **Show Image**
8. **Exit**

### Input Controls
- The program takes commands from the user to choose the desired image manipulation.

## Development Environment
- **Python**: The program is written in Python.
- **Libraries**: Uses custom helper functions from `ex5_helper` and standard libraries like `sys` and `typing`.

## How to Run

### Prerequisites
- Ensure you have Python installed on your system.

### Installation
1. Clone or download the repository containing `image_editor.py` and `ex5_helper.py`.
2. Make sure `ex5_helper.py` is in the same directory as `image_editor.py`.

### Running the Program
1. Open a terminal or command prompt.
2. Navigate to the directory containing `image_editor.py`.
3. Run the program using the following command:
   ```sh
   python image_editor.py <path_to_image>
   ```
   Replace `<path_to_image>` with the path to the image file you want to manipulate.

### Usage
- Upon running the program, a menu will appear prompting you to choose an action.
- Enter the corresponding number for the desired action:
  1. Convert to grayscale
  2. Blur the image
  3. Resize the image
  4. Rotate the image
  5. Detect edges in the image
  6. Quantize the image
  7. Show the current state of the image
  8. Exit the program
- Follow the on-screen prompts for additional input as required for each action.

## Functions

### Utility Functions
- **is_float(s)**: Checks if a string can be cast to a float.
- **separate_channels(image)**: Separates a colored image into single-channel images.
- **combine_channels(channels)**: Combines single-channel images into a colored image.
- **RGB2grayscale(colored_image)**: Converts a colored image to a grayscale image.
- **blur_kernel(size)**: Generates a blur kernel of a given size.
- **calculte(matrix, kernel)**: Calculates the convolution of a matrix and a kernel.
- **builde_box(image, i, j, size)**: Builds a submatrix around a pixel for convolution.
- **apply_kernel(image, kernel)**: Applies a kernel to an image for convolution.
- **bilinear_interpolation(image, y, x)**: Performs bilinear interpolation on an image.
- **resize(image, new_height, new_width)**: Resizes an image to new dimensions.
- **rotate_90(image, direction)**: Rotates an image by 90 degrees in the specified direction.
- **get_edges(image, blur_size, block_size, c)**: Detects edges in an image using adaptive thresholding.
- **quantize(image, N)**: Quantizes a grayscale image to N levels.
- **quantize_colored_image(image, N)**: Quantizes a colored image to N levels.

### Choice Functions
- **choice1(image, gray)**: Converts the image to grayscale if not already grayscale.
- **choice2(image, gray)**: Blurs the image with a specified kernel size.
- **choice3(image, gray)**: Resizes the image to specified dimensions.
- **choice4(image)**: Rotates the image in a specified direction.
- **choice5(image, gray)**: Applies edge detection to the image.
- **choice6(image, gray)**: Quantizes the image to a specified number of levels.

### Main Function
- **get_path()**: Retrieves and validates the image path from command-line arguments.
- **main()**: The main function that handles user input and performs the corresponding image manipulations.

## Acknowledgements
- **Instructor and Course Staff**: For guidance and support throughout the project.

