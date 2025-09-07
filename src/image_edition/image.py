import cv2
from src.debug_mode.log import AppLogger

logger = AppLogger(
    name="image_edition"
)

def get_image(path):
    logger.debug(f"Loading image from {path}")
    
    image = cv2.imread(path)

    if image is None:
        logger.error(f"Failed to load image from {path}")
        raise ValueError(f"Image at {path} could not be loaded.")
    
    logger.debug(f"Image loaded successfully from {path}")
    return image

def censor_area(image, box, pixel_size=3):
    """
    Applies pixelation censorship to a region in an image based on detection data.

    Args:
        box (List[int]): Original bounding box coordinates [x, y, w, h].
        pixel_size (int, optional): The size of the pixelation blocks. Default is 3.

    Returns:
        np.ndarray: The censored box with pixelated regions.
    """
    logger.debug(f"Censoring area with box {box} and pixel size {pixel_size}")
    x, y, w, h = box
    image_small = cv2.resize(
        image[y:y+h, x:x+w], 
        (
            w // pixel_size, 
            h // pixel_size
        ), 
        interpolation=cv2.INTER_LINEAR
    )
    logger.debug(f"Resized area to {image_small.shape[1]}x{image_small.shape[0]} for pixelation")
    image_pixelated = cv2.resize(
        image_small, 
        (w, h), 
        interpolation=cv2.INTER_NEAREST
    )
    logger.debug(f"Pixelated area resized back to original size {w}x{h}")
    return image_pixelated

def censor_image(image_data, detect_data, pixel_size=3):
    """
    Applies pixelation censorship to all detected regions in an image.
    Args:
        image_data (np.ndarray): The original image data.
        detect_data (List[Dict]): List of detection results with bounding boxes.
        pixel_size (int, optional): The size of the pixelation blocks. Default is 3.
    Returns:
        np.ndarray: The censored image data.
    """
    logger.debug(f"Censoring image with {len(detect_data)} detected regions")
    for detect in detect_data:
        box = detect['box']
        logger.debug(f"Processing box {box} for censorship")
        x, y, w, h = box
        image_data[y:y+h, x:x+w] = censor_area(
            image_data, 
            box,
            pixel_size
        )
        logger.debug(f"Censored region at {box}")
    logger.debug("Image censorship completed")   
    return image_data

def save_image(name, image, output_path='output'):
    logger.debug(f"Saving image {name} to {output_path}")
    cv2.imwrite(f"{output_path}/{name}", image)
    logger.debug(f"Image {name} saved successfully to {output_path}")
    