import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import SHARPEN

# Initialize the application
app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

# UI components
lb_image = QLabel("Image")
btn_dir = QPushButton("Folder")
lw_files = QListWidget()
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")

# Layout
row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

# Global variable
workdir = ''

# File filtering function
def filter(files, extensions):
    return [filename for filename in files if any(filename.endswith(ext) for ext in extensions)]

# Choose a working directory
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

# Display a list of files
def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

# ImageProcessor class
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, filename):
        """Load an image and store its path and filename."""
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def saveImage(self):
        """Save a copy of the image in a subfolder."""
        path = os.path.join(workdir, self.save_dir)
        if not os.path.exists(path):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def do_bw(self):
        """Convert the image to black and white."""
        self.image = self.image.convert("L")
        self.saveImage()
        self.showImage()

    def do_left(self):
        """Rotate the image 90 degrees to the left."""
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        self.showImage()

    def do_right(self):
        """Rotate the image 90 degrees to the right."""
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        self.showImage()

    def do_flip(self):
        """Flip the image horizontally."""
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        self.showImage()

    def do_sharpen(self):
        """Apply a sharpening filter to the image."""
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        self.showImage()

    def showImage(self):
        """Display the processed image on the QLabel."""
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        lb_image.hide()
        pixmapimage = QPixmap(image_path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

# Function to display the selected image
def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage()

workimage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)

# Connect buttons to their respective functions
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)

# Run the application
app.exec()
