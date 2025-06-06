import cv2
from hailo_platform import pyhailort


def run_inference(image_path, model_path):
    print(f"🔍 Loading image: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    print(f"🧠 Loading model (simulated): {model_path}")
    # Skipping pyhailort.Hef and VDevice for now since they're not exposed

    height, width = image.shape[:2]
    dummy_detection = {
        "class_id": 0,
        "confidence": 0.92,
        "bbox": [
            int(0.2 * width),
            int(0.3 * height),
            int(0.5 * width),
            int(0.6 * height),
        ],
    }
    # Draw and save annotated image
    output_path = "data/outputs/annotated_sample1.jpg"
    x1, y1, x2, y2 = dummy_detection["bbox"]
    annotated = image.copy()
    cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = f"Confidence: {dummy_detection['confidence']:.2f}"
    cv2.putText(
        annotated, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
    )
    cv2.imwrite(output_path, annotated)
    print(f"🖼️ Annotated image saved to: {output_path}")

    print(f"📦 Detected 1 object (simulated): {dummy_detection}")
    return [dummy_detection]
