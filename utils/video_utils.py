import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)  #Opens video file
    frames = []  #Stores all vid frames

    while True:
        ret, frame = cap.read()  #Read the next frame

        if not ret:
            break  #stop when no frames left

        frames.append(frame)  #Add frame to the list

    return frames  #returns all frames

def save_video(output_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #Def output format as XVID
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0])) #x and y positions x,y,x,y
    for frame in output_video_frames: #loop for each frame
        out.write(frame) #writes frame to videowriter
    out.release()




