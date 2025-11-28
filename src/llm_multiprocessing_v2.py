import time
import cv2
import os
import env
import generate_captions_and_give_alerts
from concurrent.futures import ProcessPoolExecutor, as_completed

def do_llm_analysis_on_saved_video(video_path, output_folder, interval_sec=5):
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

        # cap.read() → reads the current frame.
        # ret → True if the frame was read successfully.
        # frame → the actual image of the frame.
        ret, frame = cap.read()
        if not ret:
            break 

        filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")      # count is having the which number of frame is this
        cv2.imwrite(filename, frame)
        print(f"✅ Frame saved {filename} at {current_time:.2f} sec")

        # llm processing 
        # currentSnapshotOutput = generate_captions_and_give_alerts.generate_alert_and_give_alert(filename)
        # print("Model Output:\n", currentSnapshotOutput)
        # print("\n\n")

        with ProcessPoolExecutor(max_workers=env.MAX_WORKERS) as executor:
            futures = {executor.submit(generate_captions_and_give_alerts.generate_alert_and_give_alert, filename)}

            for future in as_completed(futures):
                result = future.result()
                print(result)

        count += 1
        current_time += interval_sec  # jump 3s forward
        time.sleep(interval_sec)

    cap.release()
    print("✅ Processing and saving of frame done")


if __name__ == "__main__":
    video_path = env.VIDEO_PATH
    output_folder = env.OUTPUT_FOLDER
    do_llm_analysis_on_saved_video(video_path, output_folder, interval_sec=env.GAP)