import json

from PySide6.QtCore import Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow
from pymongo import MongoClient

from guilib._gui import Ui_Form
from image import Image
from machine.Camera import Camera


class MainWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super(MainWindow, self).__init__() #
        self.setupUi(self)

        self.clients = MongoClient("mongodb://localhost:27017/")
        self.database = self.clients['cpr_db']
        self.collection = self.database['cpr_data']

        self.frame_num = 0
        self.ProcessCam_X = Camera(0)  # 建立相機物件
        self.ProcessCam_X.rawdata.update_image.connect(self.set_image_x)  # 槽功能：取得並顯示影像
        #
        self.ProcessCam_Y = Camera(2)  # 建立相機物件
        self.ProcessCam_Y.rawdata.update_image.connect(self.set_image_y)  # 槽功能：取得並顯示影像

        self.ProcessCam_Z = Camera(4)  # 建立相機物件
        self.ProcessCam_Z.rawdata.update_image.connect(self.set_image_z)  # 槽功能：取得並顯示影像

        self.startBtn.clicked.connect(self.startVideo)
        self.stopBtn.clicked.connect(self.stopVideo)

        self.Exit.clicked.connect(self.exit)

    @Slot(Image)
    def set_image_x(self,camera_image):
        image = QImage(camera_image, camera_image.shape[1], camera_image.shape[0],  camera_image.strides[0], QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        self.image_x.setPixmap(pix)

    @Slot(Image)
    def set_image_y(self, camera_image):
        image = QImage(camera_image, camera_image.shape[1], camera_image.shape[0], camera_image.strides[0],
                       QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        self.image_y.setPixmap(pix)

    @Slot(Image)
    def set_image_z(self, camera_image):
        image = QImage(camera_image, camera_image.shape[1], camera_image.shape[0], camera_image.strides[0],
                       QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        self.image_z.setPixmap(pix)

    #開始錄影
    def startVideo(self):
        if self.ProcessCam_X.connect:  #and self.ProcessCam_Y.connect:
            self.ProcessCam_X.running = True
            self.ProcessCam_X.open()
            self.ProcessCam_X.start()
            self.startBtn.setEnabled(True)
        if self.ProcessCam_Y.connect:
            self.ProcessCam_Y.running = True
            self.ProcessCam_Y.open()
            self.ProcessCam_Y.start()
            self.startBtn.setEnabled(True)

        if self.ProcessCam_Z.connect:
            self.ProcessCam_Z.running = True
            self.ProcessCam_Z.open()
            self.ProcessCam_Z.start()
            self.startBtn.setEnabled(True)

        self.position.setChecked(False)
        self.depth.setChecked(False)
        self.qualification.setChecked(False)
        self.startBtn.setEnabled(False)

    #結束錄影
    def stopVideo(self):
        if self.ProcessCam_X.connect:
            self.ProcessCam_X.stop()
            self.startBtn.setEnabled(True)
        if self.ProcessCam_Y.connect:
            self.ProcessCam_Y.stop()
            self.startBtn.setEnabled(True)

        if self.ProcessCam_Z.connect:
            self.ProcessCam_Z.stop()
            self.startBtn.setEnabled(True)

        data = {}
        data["x_file"] = self.ProcessCam_X.filename
        data["y_file"] = self.ProcessCam_Y.filename
        data["z_file"] = self.ProcessCam_Z.filename
        data["position"] = self.position.isChecked()
        data["depth"] = self.depth.isChecked()
        data["qualification"] = self.qualification.isChecked()
        json_data = json.dumps(data)
        self.collection.insert_one(data)
        print(json_data)

        # print("stopVideo", self.ProcessCam_X.connect)
        # print("stopVideo", self.ProcessCam_Y.connect)
        # print("stopVideo", self.ProcessCam_Z.connect)
    def exit(self):
        self.close()
