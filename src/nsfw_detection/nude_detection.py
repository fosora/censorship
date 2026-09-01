from nudenet import NudeDetector

__valid_labels__ = [
    "FEMALE_GENITALIA_COVERED", "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_COVERED", "MALE_GENITALIA_EXPOSED"
]

def detect_nude(file: str, labels: list[str] = __valid_labels__):
    """
    Detects nude content in an image file using the NudeNet model.
    Args:
        file (str): Path to the image file.
        labels (List[str], optional): List of labels to filter detections. 
            Default is all valid labels.
    Returns:
        List[Dict]: List of detection results with bounding boxes and classes.
    """
    if len(labels) == 0:
        return image

    detector = NudeDetector(
        model_path="src/nsfw_detection/models/default/640m.onnx", 
        inference_resolution=640
    )
    image = detector.detect(file)

    return [
        detect
        for detect in image
        if detect.get('class') in labels
    ]
