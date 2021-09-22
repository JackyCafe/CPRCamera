from PySide6.QtCore import Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow

from guilib._gui import Ui_Form
from image import Image
from machine.Camera import Camera


class MainWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super(MainWindow, self).__init__() #
        self.setupUi(self)
        self.frame_num = 0
        self.ProcessCam = Camera()  # 建立相機物件
        self.ProcessCam.rawdata.update_image.connect(self.set_image)  # 槽功能：取得並顯示影像

        self.startBtn.clicked.connect(self.startVideo)
        self.stopBtn.clicked.connect(self.stopVideo)

    @Slot(Image)
    def set_image(self,camera_image):
        image = QImage(camera_image, camera_image.shape[1], camera_image.shape[0],  camera_image.strides[0], QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        self.image_label.setPixmap(pix)

    #開始錄影
    def startVideo(self):
        if self.ProcessCam.connect:
            print("startVideo")
            self.ProcessCam.running = True
            self.ProcessCam.open()
            self.ProcessCam.start()
            self.startBtn.setEnabled(True)
        else:
            self.startBtn.setEnabled(False)

    #結束錄影
    def stopVideo(self):
        if self.ProcessCam.connect:
            self.ProcessCam.stop()
            self.startBtn.setEnabled(True)
        print("stopVideo",self.ProcessCam.connect)


