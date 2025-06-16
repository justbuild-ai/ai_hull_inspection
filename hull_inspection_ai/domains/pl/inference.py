from hull_inspection_ai.visual.inference_engine import run_inference


def run(image_path, model_path):
    print(f"[LV] Running inference on: {image_path}")
    print(f"[LV] Using model: {model_path}")

    detections = run_inference(image_path, model_path)
    print(f"[LV] Detections: {detections}")
