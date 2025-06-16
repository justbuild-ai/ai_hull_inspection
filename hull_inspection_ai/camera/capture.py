import site
site.addsitedir("/usr/lib/python3/dist-packages")
import cv2
import os
from datetime import datetime


def capture_image(
    output_path="data/test_images/live_capture.jpg", resolution=(640, 480)
):
    cap = cv2.VideoCapture(0)  # default camera

    if not cap.isOpened():
        raise RuntimeError("❌ Could not open camera")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    print("📸 Capturing image...")

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise RuntimeError("❌ Failed to capture image")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, frame)
    print(f"✅ Image saved to {output_path}")
    return output_path
