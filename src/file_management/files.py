import os
import json
from pathlib import Path
from src.image_data import ImageData

def get_files(
        folder_path = "files" , 
        extensions = (".jpeg", ".jpg", ".png"),
        recursive: bool = False
    ):
    """
    Returns a list of image file paths in a directory.
    Args:
        folder_path (str): Path to the directory to search for images. Default: "files".
        extensions (tuple): Allowed image file extensions. Default: (".jpeg", ".jpg", ".png").
        recursive (bool): Recursively search subdirectories when True.

    Returns:
        List[str]: List of image file paths found in the directory.
    """
    
    folder_path = Path(folder_path)
    if recursive:
        candidate_files = folder_path.rglob("*")
    else:
        candidate_files = folder_path.iterdir()

    return [
        str(file) 
        for file in candidate_files
            if 
                file.is_file() and 
                file.suffix.lower() in extensions
    ]

def save_file_data(data: list[ImageData], output_path: str = "output"):
    """
    Saves the file data to a JSON file.
    Args:
        data (List[ImageData]): List of ImageData objects to be saved.
        output_path (str): Path to the output JSON file. Default is "output/data.json".
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    json_data = [image.to_dict() for image in data]

    with open(f'{output_path}/results.json', 'w') as file:
        json.dump(json_data, file, indent=4)