import time
import cv2
import os
import env
import multiprocessing
from perplexityAi import online_llm_perplexity

def onine_llm_analysis_on_saved_video(video_path, output_folder, interval_sec=3):
    os.makedirs(output_folder, exist_ok=True)
    
    # opening the video for reading 
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps

    print(f"Video duration: {duration:.2f} seconds, FPS: {fps}\n")
    # Video duration: 34.40 seconds, FPS: 25.0, frame count: 860

    count = 0      # keeps track of how many frames we have saved.
    current_time = 0         # the time in the video (in seconds) where we will grab the next frame.

    while current_time <= duration:
        # Jump to the exact timestamp (in ms)
        cap.set(cv2.CAP_PROP_POS_MSEC, current_time * 1000)     
 
        ret, frame = cap.read()
        if not ret:
            break 

        filename = os.path.join(output_folder, f"frame_{count:04d}.jpg") # count have the number of frame it is
        cv2.imwrite(filename, frame)
        # print(f"Frame saved {filename} at {current_time:.2f} sec")

        # llm processing 
        # Create a separate process for each frame
        p = multiprocessing.Process(target=online_llm_perplexity, args=(filename,))
        p.start()

        count += 1
        current_time += interval_sec  # jump 3s forward
        time.sleep(interval_sec)

    cap.release()
    time.sleep(10)
    print("✅ Processing and saving of frame done")


if __name__ == "__main__":
    video_path = env.VIDEO_PATH
    output_folder = env.OUTPUT_FOLDER_ONLINE_LLM
    onine_llm_analysis_on_saved_video(video_path, output_folder, interval_sec=env.GAP)