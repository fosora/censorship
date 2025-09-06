import cv2

__square_color__ = (255, 255, 255)
__square_thickness__ = 2
def add_debug_square(
    image,
    box,
    thickness = __square_thickness__,
    color = __square_color__
):
    cv2.rectangle(
        image, 
        box, 
        color, 
        thickness
    )

__text_color__= (255, 255, 255)
__text_thickness__= 2
def add_debug_label(
        image, 
        position, 
        text, 
        size,
        color = __text_color__, 
        thickness = __text_thickness__
    ):
    cv2.putText(
        image, 
        text,
        position,  
        cv2.FONT_HERSHEY_SIMPLEX,
        size,
        color,
        thickness
    )

def add_debug_data(
    image_data, 
    detect_data,
    line_color = (255, 255, 255),
    thickness = 2,
    font_scale = 0.64,
    font_thickness = 2,
):
    for detect in detect_data:
        box = detect['box']
        add_debug_square(
            image_data, 
            box, 
            thickness, 
            line_color
        )
        add_debug_label(
            image_data, 
            (
                box[0],
                box[1] - 28
            ), 
            detect['class'],
            font_scale,
            font_thickness
        )
        add_debug_label(
            image_data, 
            (
                box[0],
                box[1] - (28 - 22)
            ), 
            f"{detect['score']:.2f}", 
            font_scale - (22/100),
            font_thickness
        )
        
    return image_data