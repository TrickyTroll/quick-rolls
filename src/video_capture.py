import cv2

video_capture = cv2.VideoCapture(0)
video_codec_code = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("videos/cam_video.mp4", video_codec_code, 20.0, (640,480))

while(True):
     # Capture each frame of webcam video
     ret,frame = video_capture.read()
     cv2.imshow("My cam video", frame)
     output.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break