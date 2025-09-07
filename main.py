from src.debug_mode.log import AppLogger
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
    logger = AppLogger(name="main")

    logger.info("Fetching files to process")
    files = get_files()
    if len(files) == 0:
        logger.warning("No files found to process.")
        return
    logger.info(f"Found {len(files)} files to process")

    logger.info("Loading file data")
    data = get_file_data(files)
    logger.info(f"Loaded data for {len(data)} files")

    logger.info("Starting processing of files")
    for item in data:
        logger.info(f"Processing file: {item['name']}")
        path = item['path']
        try:
            logger.info(f"Loading original image for {item['name']}")
            item['status'] = 'processing'
            item['image']['original'] = get_image(path)
            logger.info(f"Image loaded for {item['name']}")

            logger.info(f"Detecting nude content in {item['name']}")
            item['detect_data'] = detect_nude(path)
            logger.info(f"Detection completed for {item['name']} with {len(item['detect_data'])} detections")

            logger.debug(f"Detection data: {item['detect_data']}")
            add_debug_censor(item['name'], item['image'], item['detect_data'])

            logger.info(f"Censoring image {item['name']}")
            censor_image(item['name'], item['image'], item['detect_data'])
            logger.info(f"Censorship completed for {item['name']}")

            item['status'] = 'done'
            logger.info(f"Finished processing file: {item['name']}")
        except Exception as e:
            item['status'] = 'error'
            logger.error(f"Error processing file {path}: {e}")
        finally:
            logger.progress_percent("Overall Progress", data.index(item) + 1, len(data))
    logger.info("Processing completed for all files")

    #save_file_data(data)

if __name__ == "__main__":
    logger = AppLogger()
    try:
        logger.info("Starting Application...")
        main()
    except Exception as e:
        logger.error(f"Application error: {e}")
    finally:
        logger.info("Application finished.")
