from PIL import Image, ImageFile

# Allow broken images
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Characters list
symbols = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Image path
img_path = "/content/image2.jfif"

# Open image
pic = Image.open(img_path)

# Image size
width, height = pic.size

# New size
new_width = 100
ratio = height / width
new_height = int(new_width * ratio * 0.5)

# Resize image
pic = pic.resize((new_width, new_height))

# Convert to black and white
pic = pic.convert("L")

# Get pixel values
pixel_list = list(pic.getdata())

# Make matrix
matrix = []
temp_row = []

for index in range(len(pixel_list)):
    temp_row.append(pixel_list[index])

    if (index + 1) % new_width == 0:
        matrix.append(temp_row)
        temp_row = []

# Empty result
result = ""

# Step size
step = 255 // len(symbols)

# Convert pixels to ASCII
for index in range(len(pixel_list)):
    value = pixel_list[index]

    if value >= 255 - step:
        result += symbols[0]
    elif value >= 255 - step * 2:
        result += symbols[1]
    elif value >= 255 - step * 3:
        result += symbols[2]
    elif value >= 255 - step * 4:
        result += symbols[3]
    elif value >= 255 - step * 5:
        result += symbols[4]
    elif value >= 255 - step * 6:
        result += symbols[5]
    elif value >= 255 - step * 7:
        result += symbols[6]
    elif value >= 255 - step * 8:
        result += symbols[7]
    elif value >= 255 - step * 9:
        result += symbols[8]
    elif value >= 255 - step * 10:
        result += symbols[9]
    else:
        result += symbols[10]

    # New line after each row
    if (index + 1) % new_width == 0:
        result += "\n"

# Print result
print(result)

# Save to file
out_file = open("ascii_image.txt", "w")
out_file.write(result)
out_file.close()

print("Saved as ascii_image.txt")
#---------------------------------------------
