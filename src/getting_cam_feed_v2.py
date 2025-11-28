import cv2
import time
import os

# Path where you want to save frames
save_path = "/Users/aadi/Desktop/pawaac/snapshots"

# Create directory if not exists
os.makedirs(save_path, exist_ok=True)

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
        frame_count += 1
        filename = os.path.join(save_path, f"frame_{frame_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        last_saved_time = current_time

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Camera feed closed.")
