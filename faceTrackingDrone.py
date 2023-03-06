from ft_utils import *
import cv2

w, h = 360, 240
pid = [0.4, 0.4, 0]
pError = 0
startCounter = 0

myDrone = initializeTello()

while True:
    if startCounter == 0:
        myDrone.takeoff()
        myDrone.send_rc_control(0, 0, 25, 0)
        startCounter = 1

        img = telloGetFrame(myDrone, w, h)
        img, info = findFace(img)
        pError = trackFace(myDrone, info, w, pid, pError)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            myDrone.land()
            break
