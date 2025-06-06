from hull_inspection_ai.visual.inference_engine import run_inference

def run(image_path, model_path):
    print("[LV] Running Hailo inference pipeline...")
    results = run_inference(image_path, model_path)

    for det in results:
        print(f"[LV] Detection: {det}")
