import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from scipy.ndimage import binary_dilation, binary_erosion

class ImageProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.dilation_size = 1
        self.erosion_size = 1
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Processing App")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        self.dilation_slider = QSlider(Qt.Horizontal)
        self.dilation_slider.setMinimum(1)
        self.dilation_slider.setMaximum(10)
        self.dilation_slider.setValue(self.dilation_size)
        self.dilation_slider.valueChanged.connect(self.on_dilation_slider_change)
        layout.addWidget(self.dilation_slider)

        self.erosion_slider = QSlider(Qt.Horizontal)
        self.erosion_slider.setMinimum(1)
        self.erosion_slider.setMaximum(10)
        self.erosion_slider.setValue(self.erosion_size)
        self.erosion_slider.valueChanged.connect(self.on_erosion_slider_change)
        layout.addWidget(self.erosion_slider)

        self.setLayout(layout)

    def load_image(self, image_path):
        self.image = plt.imread(image_path)
        self.update_display()

    def on_dilation_slider_change(self, value):
        self.dilation_size = value
        self.update_display()

    def on_erosion_slider_change(self, value):
        self.erosion_size = value
        self.update_display()

    def update_display(self):
        if self.image is not None:
            dilated_image = binary_dilation(self.image, iterations=self.dilation_size)
            eroded_image = binary_erosion(self.image, iterations=self.erosion_size)

            combined_image = np.hstack((self.image, dilated_image, eroded_image))

            q_img = QImage(combined_image.data, combined_image.shape[1], combined_image.shape[0],
                           combined_image.strides[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessingApp()
    window.load_image("/Users/bizzarohd/Desktop/Screenshot 2023-08-02 at 8.06.07 PM.png")  # Replace with your image path
    window.show()
    sys.exit(app.exec_())
