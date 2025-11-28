import time
import cv2
import os
import env
import generate_captions_and_give_alerts
import multiprocessing


def do_llm_analysis_on_cam_feed(video_path, output_folder, interval_sec=5):
    os.makedirs(output_folder, exist_ok=True)
    
    # opening the video for llm analysis
    # Open the default camera (usually 0)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Track last saved time
    last_saved_time = time.time()
    frame_count = 0

    print("Press 'q' to quit...")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the live camera feed
        cv2.imshow('Camera Feed', frame)

        # Save frame every 3 seconds
        current_time = time.time()
        if current_time - last_saved_time >= 3:   # saving frame at every 3 sec
            filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(filename, frame)
            # print(f"Saved: {filename}")  # distrubing the alert messages

            # llm processing 
            # Create a separate process for each frame
            p = multiprocessing.Process(target=generate_captions_and_give_alerts.generate_alert_and_give_alert, args=(filename,))
            p.start()
            # processes.append(p)

            last_saved_time = current_time
            frame_count += 1

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Camera feed closed.")
    time.sleep(10)
    print("✅ Processing and saving of frame done")


if __name__ == "__main__":
    video_path = env.VIDEO_PATH
    output_folder = env.OUTPUT_FOLDER
    do_llm_analysis_on_cam_feed(video_path, output_folder, interval_sec=env.GAP)