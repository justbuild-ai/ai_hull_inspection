import numpy as np
import hull_inspection_ai.postprocess.yolo_postprocess as yolo_postprocess
from . import yolo_postprocess


def decode_yolo_bin(bin_path, image_shape, anchors=None, num_classes=80):
    """
    Decodes raw .bin output from Hailo using YOLO-style postprocessing.
    Returns a list of detections.
    """
    with open(bin_path, "rb") as f:
        raw_data = f.read()

    float_data = np.frombuffer(raw_data, dtype=np.float32)

    # Example for yolov8s: [num_detections, 85] (x, y, w, h, obj, cls0..cls79)
    detections = float_data.reshape((-1, 85))

    boxes = yolo_postprocess.non_max_suppression(
        predictions=[detections],
        conf_thres=0.25,
        iou_thres=0.45,
        classes=None,
        agnostic=False,
    )

    return boxes[0]  # list of [x1, y1, x2, y2, conf, cls]
