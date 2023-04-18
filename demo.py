import cv2

def capture_video_stream(url):
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Error opening video stream")
        return None
    return cap

url = 0
cap = capture_video_stream(url)
while cap is not None:
    ret, frame = cap.read()
    if ret:
        # Process the frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()