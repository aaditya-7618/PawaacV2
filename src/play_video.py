import cv2
import os
import env

IS_VIDEO_OPEN = False

def set_video_open_status(value):
    IS_VIDEO_OPEN = value


def play_video(video_path):
    IS_VIDEO_OPEN = True
    print("🎥 Attempting to open video:", video_path)

    if not os.path.exists(video_path):
        print("❌ Video file does NOT exist at path!")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ OpenCV FAILED to open the video.")
        return

    while True:
        ret, frame = cap.read()
        # ❌ If frame could not be read → STOP
        if not ret:
            print("⚠️ No more frames. Video ended or failed to read.")
            break

        cv2.imshow("Video Playback", frame)

        # ✅ IMPORTANT: Must be >= 1 or window will freeze/close
        key = cv2.waitKey(30) & 0xFF

        if key == ord('q') or IS_VIDEO_OPEN == False:
            print("🛑 'q' pressed. Closing video.")
            break

    cap.release()
    cv2.destroyAllWindows()

print(play_video(env.VIDEO_PATH))
