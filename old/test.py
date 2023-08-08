import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage,QPainter
from PyQt5.QtCore import Qt, QPointF, QRectF


class ZoomableImageViewer(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        self.image = QImage(image_path)
        self.pixmap = QPixmap.fromImage(self.image)
        self.scale = 1.0
        self.cursor_position = None

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.view = QGraphicsView(self.central_widget)
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)

        self.scene.addPixmap(self.pixmap)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.view)

        self.view.viewport().installEventFilter(self)
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.show_image()

    def show_image(self):
        size = self.image.size() * self.scale
        scaled_pixmap = self.pixmap.scaled(size)

        if self.cursor_position:
            self.view.setSceneRect(QRectF(self.cursor_position - size / 2, size))
        else:
            self.view.setSceneRect(QRectF(QPointF(0, 0), size))

        self.view.fitInView(self.view.sceneRect(), Qt.KeepAspectRatio)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Wheel:
            self.cursor_position = self.view.mapToScene(event.pos())
            if event.angleDelta().y() > 0:
                self.scale *= 1.1
            else:
                self.scale /= 1.1

            self.show_image()
            return True

        return super().eventFilter(source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_path = '/Users/bizzarohd/Desktop/MagScopeTracker.png'  # Replace with your image path
    viewer = ZoomableImageViewer(image_path)
    viewer.show()
    sys.exit(app.exec_())

   




  def wheelEvent(self, event: QWheelEvent):

        scroll_amount = event.angleDelta().y()
        scroll_direction = "Up" if scroll_amount > 0 else "Down"
        print(f"Scroll Amount: {scroll_amount}, Scroll Direction: {scroll_direction}")
        pos = event.pos()
        self.curserx = pos.x()
        self.cursery = pos.y()
        self.zoom = scroll_amount