import os
import sys

def getResourcePath(relativePath):
    try:
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(os.path.dirname(__file__))
    
    return os.path.join(basePath, relativePath)