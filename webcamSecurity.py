
import cv2

def take_snapshot():
     # initializing cv2,
    # used to start the webcam
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        # read the frames while the camera is on
        # ret is a dummy variable which returns a boolean value (T or F), to tell us if something is being returned or not
        # frame has the frames of the video (images)
        ret,frame = videoCaptureObject.read()
        # Syntax: cv2.imwrite(filename, image)
        # filename: A string representing the file name. The filename must include image format like .jpg, .png, etc. -image: It is the image that is to be saved.
        # this method is used to save a image into any storage device
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture2.jpg",frame)
        result = False

     # release the camera/stop the webcam
    videoCaptureObject.release()
    # now close all the windows that might be opened whilst this process
    cv2.destroyAllWindows()

take_snapshot()
    
    

