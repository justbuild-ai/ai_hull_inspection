import cv2
import subprocess
import tempfile
import os
from hull_inspection_ai.postprocess.bin_decoder import decode_yolo_bin


def run_inference(image_path, model_path):
    print(f"🔍 Loading image: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    # Convert image to raw RGB format expected by Hailo
    rgb_path = _convert_to_raw_rgb(image, image_path)

    output_bin = "data/outputs/sample1_out.bin"

    cmd = [
        "hailortcli",
        "run",
        "--hef",
        model_path,
        "--input",
        rgb_path,
        "--output",
        output_bin,
        "--timeout",
        "3000",
    ]

    print(f"🚀 Running Hailo CLI: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("[❌] Hailo inference failed:")
        print(result.stderr)
        return []

    print("[✅] Hailo CLI completed.")

    # Run YOLO bin decoder
    detections = decode_yolo_bin(output_bin, image.shape)

    # Draw and return all detections
    output_path = "data/outputs/annotated_sample1.jpg"
    annotated = image.copy()

    for det in detections:
        x1, y1, x2, y2, conf, cls = map(int, det)
        label = f"Anomaly Detected {cls + 1} ({conf:.2f})"
        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            annotated,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )

    cv2.imwrite(output_path, annotated)
    print(f"🖼️ Annotated image saved to: {output_path}")
    return detections.tolist()


def _convert_to_raw_rgb(image, original_path):
    """
    Saves a BGR OpenCV image to a raw RGB file as required by Hailo CLI.
    """
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rgb_path = os.path.splitext(original_path)[0] + ".rgb"
    with open(rgb_path, "wb") as f:
        f.write(rgb_image.tobytes())
    print(f"🧾 Saved raw RGB to: {rgb_path}")
    return rgb_path
