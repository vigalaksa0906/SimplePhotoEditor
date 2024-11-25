# Easy Editor

**Easy Editor** is a simple image editing application built using Python and PyQt5. It allows users to perform basic image editing tasks like rotating, flipping, sharpening, and converting images to black and white.

## Features
- **Folder Selection**: Load a directory and display a list of image files.
- **Image Preview**: View the selected image with its modifications.
- **Basic Editing Tools**:
  - Rotate left
  - Rotate right
  - Flip horizontally
  - Sharpen
  - Convert to black and white
- **Automatic Save**: Edited images are saved in a `Modified/` subfolder within the working directory.

## Requirements
- Python 3.7 or later
- Libraries:
  - PyQt5
  - Pillow (PIL)
## Installation
1. Clone the repository
2. Install the required Python libraries:
   ```bash
   pip install PyQt5 Pillow
   ```
## Usage
1. Run the application:
```bash
python main.py
```
2. Use the Folder button to select a directory containing images.
3. Select an image from the list to preview it.
4. Use the editing buttons to modify the image
5. Edited images will be automatically saved in the Modified/ subfolder
