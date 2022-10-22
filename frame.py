import numpy as np 
import cv2
import time 

default_kernel = -1*np.ones((3,3))
default_kernel[1,1] = 8

class frame:
    """ Class describing a single frame of the desired output """
    def __init__(self, kernel = default_kernel):
        """ Initialized the frame class """
        cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(
                "preview",
                cv2.WND_PROP_FULLSCREEN,
                cv2.WINDOW_FULLSCREEN)

        self.vc = cv2.VideoCapture(0) # , cv2.CAP_DSHOW)
        #self.vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        #self.vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.rval, self.input = self.vc.read()
        self.frame = np.zeros((np.shape(self.input)[0],
                               np.shape(self.input)[1]))
        self.input_processed = np.zeros(np.shape(self.frame))
        self.frame_nr = 0
        self.previous_frames = np.zeros(np.shape(self.frame))
        self.kernel = np.array(kernel)

    def refresh_input(self):
        """ Loads a new input frame """
        self.rval, self.input = self.vc.read()

    def normalize_and_blur(self):
        """ Prepares the input image for further processing """
        gray = cv2.cvtColor(self.input, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, 5)
        self.frame = cv2.threshold(gray_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    def edge_detection(self):
        """ Determines regions of contrast in the picture """
        self.frame = cv2.filter2D(self.frame, -1, self.kernel)

    def trailing(self):
        """ Creates a trailing effect of moving objects """

    def display_frame(self):
        cv2.imshow("output", self.frame)
        self.frame_nr += 1

