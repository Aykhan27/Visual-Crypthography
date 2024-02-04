# Image Merge Tool

This Python script allows you to merge multiple PNG images into a single combined image using the concept of visual cryptography. The merged image can be used to reveal the original image by superimposing two or more encrypted images.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3.x
- Pillow (PIL) library (`pip install pillow`)

## Getting Started

1. Clone this repository or download the `image_merge.py` script.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```bash
   python image_merge.py
   ```

## Usage

1. The script will prompt you to enter the number of PNG files you want to merge.

2. Enter the file paths of the PNG images you want to merge. The images should be of the same size.

3. The script will combine the images and save the resulting merged image as 'combined_image.png' in the same directory.

4. The merged image will be displayed using the default image viewer on your system.

## Example

Suppose you want to merge two scrambled PNG images: `scrambled1.png` and `scrambled2.png`. Here's how you can use the script:

1. Enter `2` as the number of PNG files to merge.

2. Enter the file paths of the two images:

   ```
   Enter the file path of PNG image 1: scrambled1.png
   Enter the file path of PNG image 2: scrambled2.png
   ```

3. The script will generate a combined image and save it as 'combined_image.png' in the same directory.

4. The merged image will be displayed on your screen.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses the Pillow (PIL) library for image processing.
