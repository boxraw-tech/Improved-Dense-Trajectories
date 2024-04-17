import numpy as np
import cv2

a = np.load('features2/output-trajectory.npy')
print( a.dtype )


path = 'data/output.mp4'

show_trajectories = False
while True:
    cap = cv2.VideoCapture(path)
    
    for ix in range(15):
        ret, frame = cap.read()
        #cv2.imshow('', frame)
        #key = cv2.waitKey(0)
        #if key == ord('q'):
        #    raise SystemExit
    
    
    for a_ix in range(len(a)):
        frame_num = a[a_ix]['frame_num']
        coords = a[a_ix]['coords']
    
        if show_trajectories: 
            # draw the trajectory on the 
            for ix in range(1,14):
                coord_start = list(map(int, coords[ix-1]))
                coord_end = list(map(int, coords[ix]))
                colour = (0, 0, 255) if ix == 13 else (0, 255, 0)
                cv2.line(frame, coord_start, coord_end, colour, 1)
    
    cv2.imshow('', frame)
    key = cv2.waitKey(0)
    if key == ord('q'):
        raise SystemExit
    show_trajectories = not show_trajectories
            
