from frame import frame 
import cv2


if __name__ == "__main__":
    frame = frame()

    while frame.rval:
        frame.refresh_input()
        frame.normalize_and_blur()
        frame.edge_detection()
        frame.display_frame()

        # enable key input to stop the application
        key = cv2.waitKey(20) 
        if key == 27: # exit on ESC
            break
