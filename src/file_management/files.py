from pathlib import Path
from typing import List

def get_files(
        folder_path = Path("files") , 
        extensions = (".jpeg", ".jpg", ".png")
    ):
    """
    Returns a list of image file paths in a directory.
    Args:
        folder_path (str): Path to the directory to search for images. Default: "files".
        extensions (tuple): Allowed image file extensions. Default: (".jpeg", ".jpg", ".png").

    Returns:
        List[str]: List of image file paths found in the directory.
    """
    return [
        str(file) 
        for file in folder_path.iterdir() 
            if 
                file.is_file() and 
                file.suffix.lower() in extensions
    ]

def get_file_data(files: List[str]):
    """

    Args:  
        files (List[str]): List of image file paths to be analyzed.
        labels (List[str], optional): List of labels to filter the detection results. If not provided, uses the default labels:  
            [  
                "FEMALE_GENITALIA_COVERED", "FEMALE_GENITALIA_EXPOSED",  
                "MALE_GENITALIA_COVERED", "MALE_GENITALIA_EXPOSED",  
                "ANUS_EXPOSED", "ANUS_COVERED",  
            ]
    
    Returns:  
        List[dict]: A list of dictionaries, each representing an image and its detection results.  
        Each dictionary contains:  
            - 'name': The name of the image file.
            - 'path': The file path of the image.  
            - 'image': A dictionary with keys both set to None as default
                - 'original' 
                - 'censored'
            - 'detect_data': A list of detection dictionaries for the image, filtered by the specified labels.  
                Each detection dictionary includes information such as:  
                    - 'class': The detected label/class.  
                    - 'score': Confidence score of the detection.  
                    - 'box': Bounding box coordinates of the detected region.  
    """
    return [
        {
            "name": Path(file).name,
            "path": file,
            "detect_data": [],
            "image": {
                "original": None,
                "debug": None,
                "censored": None,
            },
            "status": "pending",
        }
        for file in files
    ]

def save_file_data(data: List[dict], output_path: str = "output/data.json"):
    import json
    with open(output_path, 'w') as f:
        #TODO: change to save only necessary data
        # filepath instead of image data
        json.dump(data, f, indent=4)