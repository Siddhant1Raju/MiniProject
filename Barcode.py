from imutils.video import VideoStream
from pyzbar import pzybar
import argparse
import datetime
import imutils
import time
import cv2
import streamlit as st





st.title("Barcode Scanner")
class VideoTransformer():
    

    #Constructing The argument parser and parse the arguments
    ap=argparse.ArgumentParser()
    ap.add_argument("-o","--output",type=str , default="barcodes.csv",help="path to output CSV file containing barcodes")
    args=vars(ap.parse_args())


    #initializing the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream")
    vs = VideoStream(src=0).start()
    time.sleep(2.0)


    #Opening the output CSV file for writing and intialize the set of 
    #barcodes found thus far
    csv = open(args["output"],"w")
    found = set()


    while True:
        frame=vs.read()
        frame=imutils.resize(frame , width=400)
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            (x,y,w,h)=barcode.rect
            cv2.rectangle(frame ,(x,y),(x+w , y+h),(0,0,255),2)

            #The barcode data is a bytes object so if we want to draw it on our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            #draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData , barcodeType)
            cv2.putText(frame, text, (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

            if barcodeData not in found:
                csv.write("{},{}\n".format(datetime.datetime.now(),barcodeData))
                csv.flush()
                found.add(barcodeData)

        #Shows the output frame
        cv2.imshow("Barcode Scanner",frame)
        key=cv2.waitkey(1) & OxFF
        if key==ord("q"):
            break

    print("[INFO] cleaning up....")
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()

    
    
webrtc_streamer(key="example",video_processor_factory=VideoTransformer)



