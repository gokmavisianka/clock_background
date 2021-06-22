from datetime import datetime
import numpy as np
import cv2
import ctypes
import time
import os


class ClockBacground:
    def get_time(self):
        self.time = datetime.now().strftime("%H:%M:%S")
        H, M, S = int(self.time[0:2]), int(self.time[3:5]), int(self.time[6:8])
        if len(str(S)) == 1: S = "0" + str(S)
        if len(str(M)) == 1: M = "0" + str(M)
        return f"{H}.{M}.{S}"

    def create_background(self):
        # This function creates a blank image.
        # You can edit the resolution, Current is 1920*1080
        self.background = np.zeros(shape=[1080, 1920, 3], dtype=np.uint8)

    def set_background(self):
        self.create_background()
        # You can edit the font size which is 10 here.
        cv2.putText(self.background, self.get_time(), (250, 600), cv2.FONT_HERSHEY_DUPLEX, 10, (255, 255, 255, 255), 2,
                    cv2.LINE_4)
        cv2.imwrite("background.png", self.background)
        path = os.path.abspath("background.png")

        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


CB = ClockBacground()


def main():
    while True:
        CB.set_background()
        time.sleep(0.95)


main()
