from PIL import Image
import numpy as np

# Ask for the number of PNG files to merge
num_images = int(input("How many PNG files do you want to merge? "))

# Initialize an empty list to store image paths
image_paths = []

# Ask for the file paths of the PNG images to be merged
for i in range(num_images):
    file_path = input("Enter the file path of PNG image {i + 1}: ")
    image_paths.append(file_path)

# Ensure all images are the same size
image_sizes = set()
for path in image_paths:
    im = Image.open(path)
    image_sizes.add(im.size)

if len(image_sizes) != 1:
    raise ValueError("Images are not the same size")

# Load and convert images to numpy arrays
image_arrays = []
for path in image_paths:
    im = Image.open(path)
    image_arrays.append(np.array(im))

# Create a new empty array with the same size and type as the input images
combined_arr = np.zeros_like(image_arrays[0])

# Combine the images
for arr in image_arrays:
    combined_arr = np.clip(combined_arr + arr, 0, 255)

# Convert back to an image
combined_img = Image.fromarray(combined_arr.astype('uint8'), 'RGB')

# Save the combined image
combined_img.save('combined_image.png')

combined_img.show()
