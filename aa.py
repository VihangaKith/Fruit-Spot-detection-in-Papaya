import cv2
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog

import os
r = tk.Tk()

def opefile():
   result= filedialog.askopenfile(initialdir="/" , title="select file",filetypes=(("MP4 files",".mp4"),("all files","*.*")))
   #print(result);
   label = Label(r,text="Video path").pack()
   #enty=Entry(r,text).pack()
   labe2 = Label(r, text=result).pack()

r.title('Import Video...')
button1 = tk.Button(r, text='Open', width=50, command=opefile).pack()
button2 = tk.Button(r, text='Close', width=50, command=r.destroy).pack()
r.geometry("750x150")
r.mainloop()



def video_to_frames(result, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    count =0
    try:

        os.mkdir(output_loc)

    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(result)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1

    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n")
    os.startfile(output_loc)
    # Start converting the video
    while cap.isOpened():
        # Extract the frame

        ret, frame = cap.read()
        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if(count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            os.startfile(output_loc)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break

if __name__=="__main__":

    # input_loc = 'C:\\Users\\Vihz\\Desktop\\pythonSource\\papaw.mp4'
    output_loc = 'D:\\Education\\3rd Year\\3rd Year Project\\Project\\Papaw\\data'
    # video_to_frames(input_loc, output_loc)