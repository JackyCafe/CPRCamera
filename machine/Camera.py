import time

from PySide6.QtCore import QThread
import cv2

from guilib.signal_container import SignalContainer


class Camera(QThread):
    def __init__(self):
        super(Camera, self).__init__()
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.rawdata = SignalContainer()
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')


        if self.cap is None or not self.cap.isOpened():
            self.running = False
            self.connect = False
        else:
            self.connect = True
            self.running = False

    def run(self) -> None:
        """ 執行多執行緒
           - 讀取影像
           - 發送影像
           - 簡易異常處理
        """

        while self.running and self.connect:
            ret , frame = self.cap.read()
            if ret:
                self.rawdata.update_image.emit(frame) #發
                self.out.write(frame)
            else:
                print("Warning!!!")
                self.connect = False

    def open(self):
        """ 開啟攝影機影像讀取功能 """
        if self.connect:
            self.running = True  # 啟動讀取狀態
            timestr = time.strftime("%Y%m%d-%H%M%S")
            self.filename = 'cpr' + timestr + '.avi'
            self.out = cv2.VideoWriter(self.filename, self.fourcc, 20.0, (800, 600))

    def stop(self):
        """ 暫停攝影機影像讀取功能 """
        if self.connect:
            self.running = False  # 關閉讀取狀態
            # self.cap.release()
            self.out.release()

    def close(self):
        """ 關閉攝影機功能 """
        if self.connect:
            self.running = False  # 關閉讀取狀態
            time.sleep(1)
