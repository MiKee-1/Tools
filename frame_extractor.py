import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim

def extract_unique_frames(video_path, output_folder, similarity_threshold=0.90):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cap = cv2.VideoCapture(video_path)
    success, prev_frame = cap.read()
    frame_count = 0
    saved_count = 0
    
    if success:
        prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(output_folder, f"frame_{saved_count:04d}.jpg"), prev_frame)
        saved_count += 1
    
    while success:
        success, frame = cap.read()
        if not success:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        similarity = ssim(prev_gray, gray)
        
        if similarity < similarity_threshold:
            cv2.imwrite(os.path.join(output_folder, f"frame_{saved_count:04d}.jpg"), frame)
            prev_gray = gray
            saved_count += 1
        
        frame_count += 1
    
    cap.release()
    print(f"Processed {frame_count} frames, saved {saved_count} unique frames.")

video_path = ".\\videos\\Video"  # path to video
output_folder = "frames_output"  # path to output folder
extract_unique_frames(video_path, output_folder)
