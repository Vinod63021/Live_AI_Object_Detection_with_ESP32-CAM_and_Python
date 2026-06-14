import cv2

# --- Use the exact same URL here ---
url = 'http://192.168.1.101:81/stream'

print("Attempting to connect to stream...")
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open video stream with OpenCV.")
    print("Check the URL, your network, and any security software.")
else:
    print("Success! Stream opened.")
    # Read one frame to confirm
    ret, frame = cap.read()
    if ret:
        print("Successfully read a frame from the stream.")
        cv2.imshow("Test Frame", frame)
        print("Press any key to close the window.")
        cv2.waitKey(0)
    else:
        print("Stream opened, but failed to read a frame.")

cap.release()
cv2.destroyAllWindows()