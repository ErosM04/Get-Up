import cv2 as c
cam_port = 0 #inizialize the cam

def take_photo():
    cam = c.VideoCapture(cam_port) #capture the video
    result, image = cam.read() #read the input

    if result: #if the result was positive
        c.imwrite("img0.png", image)
    else:
        print("failed")
    cam.release()

take_photo()