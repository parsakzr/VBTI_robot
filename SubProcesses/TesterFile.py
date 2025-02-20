import jsonHandler as jh
import random
import datetime
import numpy as np
import camerModule as cm
import parameters as p
import DataVisualisation as dv

"""
Random JSON generation
# shapes of arrays
rgbShape = (720, 1280, 3)
depthShape = (720, 1280)

# create Pos
Xpos = random.randint(0, 100)
Ypos = random.randint(0, 100)
Zpos = random.randint(0, 100)

# create caputure
RGBarray = np.random.randint(0, 255, rgbShape)
Deptharray = np.random.randint(0, 2000, depthShape)
TimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
"""
"""
# Init camera
print("Camera initialized: " + str(cm.initCamera()))

# Capture image
Deptharray, RGBarray = cm.Capture()
Xpos = Ypos = Zpos = 1
TimeStamp = datetime.datetime.now().strftime(p.dateformatting)

# Structure of the JSON file containing capture information
dict = {"Xpos": Xpos,
        "YPos": Ypos,
        "ZPos": Zpos,
        "RGBarray": RGBarray.tolist(),
        "Deptharray": Deptharray.tolist(),
        "TimeStamp": TimeStamp
        }

jh.saveDict2Json(dict)
"""
dv.showCapture()


exit()
