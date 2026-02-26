import sys
import os

WIN_WIDTH = 1000
WIN_HEIGHT = 700
FPS = 60

C_RED = (90, 0, 0)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 255, 0)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', relative_path)