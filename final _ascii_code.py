
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("C:\\Windows\\Fonts\\lucon.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg = "white"
# bg = "black"
if bg == "white":
    bg_code = 255
elif bg == "black":
    bg_code = 0

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300



#I have applied method 2 from sketch file to convert my image into sketch format

import cv2
img = cv2.imread("deepak.jpg")
grey_filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur =  cv2.GaussianBlur(invert, (41,41), 0)
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(grey_filter,invertedblur, scale = 256.0)
cv2.imwrite("sketchoutput.jpg",sketch_filter)

# Extracting height and width from Image
height, width = sketch_filter.shape

# Defining height and width of each cell==pixel
cell_w = width / num_cols
cell_h = scale * cell_w
num_rows = int(height / cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = font.getsize("A")
out_width = char_width * num_cols
out_height = scale * char_height * num_rows

# Making a new Image using PIL
out_image = Image.new("L", (out_width, out_height), bg_code)
draw = ImageDraw.Draw(out_image)

# Mapping the Characters
for i in range(num_rows):
    min_h = min(int((i + 1) * cell_h), height)
    row_pix = int(i * cell_h)

    # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
    # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
    line = "".join([char_list[
        min(int(
            np.mean(sketch_filter[row_pix:min_h, int(j*cell_w)
                    :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
        ), num_chars - 1)]
        for j in range(num_cols)]) + "\n"

    # Draw string at a given position (x,y)
    draw.text((0, i * char_height), line, fill=255-bg_code, font=font)

# Inverting Image and removing excess borders
if bg == "white":
    cropped_image = ImageOps.invert(out_image).getbbox()
elif bg == "black":
    cropped_image = out_image.getbbox()

# Saving the new Image
out_image = out_image.crop(cropped_image)
out_image.save("final_output.jpg")