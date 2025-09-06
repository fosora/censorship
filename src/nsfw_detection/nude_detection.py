from nudenet import NudeDetector
# docs : https://github.com/notAI-tech/NudeNet

__valid_labels__ = [
    "FEMALE_GENITALIA_COVERED", "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_COVERED", "MALE_GENITALIA_EXPOSED",
    "ANUS_EXPOSED", "ANUS_COVERED",
]

def detect_nude(file, labels = __valid_labels__):
    detector = NudeDetector(
        model_path="src/nsfw_detection/models/640m.onnx", 
        inference_resolution=640
    )
    image = detector.detect(file)
    if(len(labels) == 0):
        return image
    
    return [
        detect 
        for detect in image 
            if detect['class'] in labels
    ]
