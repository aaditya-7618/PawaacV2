import subprocess
import time
import cv2
import os
import env
import generate_captions_and_give_alerts

def save_frames_every_n_seconds(video_path, output_folder, interval_sec=5):
    os.makedirs(output_folder, exist_ok=True)
 
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps

    print(f"Video duration: {duration:.2f} seconds, FPS: {fps}")

    count = 0
    current_time = 0

    while current_time <= duration:
        # Jump to the exact timestamp (in ms)
        cap.set(cv2.CAP_PROP_POS_MSEC, current_time * 1000)

        ret, frame = cap.read()
        if not ret:
            break

        filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ Frame saved {filename} at {current_time:.2f} sec")

        # llm processing 
        currentSnapshotOutput = generate_captions_and_give_alerts.generate_alert_and_give_alert(filename)
        print("Model Output:\n", currentSnapshotOutput)
        print("\n\n")

        count += 1
        current_time += interval_sec  # jump 3 sec
        time.sleep(interval_sec)

    cap.release()
    print("✅ Processing and saving of frame done")


if __name__ == "__main__":
    video_path = env.VIDEO_PATH
    output_folder = env.OUTPUT_FOLDER
    save_frames_every_n_seconds(video_path, output_folder, interval_sec=env.GAP)