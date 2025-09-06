from src.file_management.files import get_file_data, get_files, save_file_data
from src.image_edition.image import get_image, save_image
from src.nsfw_detection.nude_detection import detect_nude

def censor_image(name, image_data, detect_data):
    image_data['censored'] = image_data['original'].copy()
    from src.image_edition.image import censor_image
    image_data['censored'] = censor_image(image_data['censored'], detect_data)
    save_image(name, image_data['censored'], output_path='output/censored')

def add_debug_censor(name, image_data, detect_data):
    image_data['debug'] = image_data['original'].copy()
    from src.debug_mode.debug import add_debug_data
    image_data['debug'] = add_debug_data(image_data['debug'], detect_data)
    save_image(name, image_data['debug'], output_path='output/debug')

def main():
    files = get_files()
    data = get_file_data(files)

    for item in data:
        path = item['path']
        try:
            item['status'] = 'processing'
            item['image']['original'] = get_image(path)
            item['detect_data'] = detect_nude(path)
            add_debug_censor(item['name'], item['image'], item['detect_data'])
            censor_image(item['name'], item['image'], item['detect_data'])
            item['status'] = 'done'
        except Exception as e:
            item['status'] = 'error'
            print(f"Error processing file {path}: {e}")
    
    #save_file_data(data)

if __name__ == "__main__":
    main()