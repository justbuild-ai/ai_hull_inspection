from hull_inspection_ai.visual.inference_engine import run_inference
from hull_inspection_ai.camera.capture import capture_image
from datetime import datetime


def run(image_path, model_path, live=False):
    domain_name = "PL"  # change to SV or PL as appropriate
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    print(f"[{domain_name}] Starting inference at {timestamp}...")

    if live:
        print("📸 Capturing image from camera...")
        image_path = capture_image(
            output_path=f"data/test_images/{domain_name}_{timestamp}.jpg"
        )

    print(f"[{domain_name}] Using model: {model_path}")
    print(f"[{domain_name}] Input image: {image_path}")

    detections = run_inference(
        image_path, model_path, domain=domain_name, timestamp=timestamp
    )

    print(f"[{domain_name}] Detections: {detections}")
