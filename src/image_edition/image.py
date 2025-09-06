import cv2

def get_image(path):
    return cv2.imread(path)

def censor_area(image, box, pixel_size=3):
    """
    Applies pixelation censorship to a region in an image based on detection data.

    Args:
        box (List[int]): Original bounding box coordinates [x, y, w, h].
        pixel_size (int, optional): The size of the pixelation blocks. Default is 3.

    Returns:
        np.ndarray: The censored box with pixelated regions.
    """
    x, y, w, h = box
    image_small = cv2.resize(
        image[y:y+h, x:x+w], 
        (
            w // pixel_size, 
            h // pixel_size
        ), 
        interpolation=cv2.INTER_LINEAR
    )
    image_pixelated = cv2.resize(
        image_small, 
        (w, h), 
        interpolation=cv2.INTER_NEAREST
    )
    return image_pixelated

def censor_image(image_data, detect_data, pixel_size=3):
    for detect in detect_data:
        box = detect['box']
        x, y, w, h = box
        image_data[y:y+h, x:x+w] = censor_area(
            image_data, 
            box,
            pixel_size
        )
    return image_data

def save_image(name, image, output_path='output'):
    cv2.imwrite(f"{output_path}/{name}", image)
    