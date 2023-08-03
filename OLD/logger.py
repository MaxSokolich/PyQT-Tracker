import cv2
video_width, video_height = 1000,1000

result = cv2.VideoWriter(
                    "~/Desktop/test3e32.mp4",
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    20,    
                    (video_width, video_height), ) 
result.write()
result.release()