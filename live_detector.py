import cv2
from ultralytics import YOLO
import tkinter as tk # Library to get screen size

# --- Automatically get screen resolution ---
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
# --- --- --- --- --- --- --- --- --- --- ---

# Load a pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')

# --- This should be the correct URL you found ---
url = 'http://192.168.1.101:81/stream'
# --- --- --- --- --- --- --- --- --- --- --- ---

# Create a VideoCapture object
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# --- Create a named window and set it to fullscreen ---
window_name = "YOLOv8 Live Detection"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# --- --- --- --- --- --- --- --- --- --- --- --- --- ---

print("Connecting to video stream... Press 'q' to quit fullscreen.")

# Loop through the video frames
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # If a frame was successfully read
    if ret:
        # Run YOLOv8 detection on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Resize the frame to fit the screen
        resized_frame = cv2.resize(annotated_frame, (screen_width, screen_height))

        # Display the resized frame in the fullscreen window
        cv2.imshow(window_name, resized_frame)

        # Wait for 1 millisecond, and break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        # Break the loop if the stream ends
        print("Stream disconnected.")
        break

# Release the capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
print("Stream closed and resources released.")