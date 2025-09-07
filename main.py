from src.args import get_args
from src.debug_mode.debug import add_debug_data
from src.debug_mode.log import AppLogger
from src.file_management.files import get_file_data, get_files, save_file_data
from src.image_edition.image import get_image, save_image, censor_image
from src.nsfw_detection.nude_detection import detect_nude

def main(args):   
    logger = AppLogger(
        name="main",
        level="DEBUG" if args.debug else "INFO"
    )

    logger.info("Fetching files to process")
    files = get_files(args.input)
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
            original_image = get_image(path)
            item['image']['original'] = {
                'data': original_image,
                'path': path
            }
            logger.info(f"Image loaded for {item['name']}")

            logger.info(f"Detecting nude content in {item['name']}")
            item['detect_data'] = detect_nude(path)
            logger.info(f"Detection completed for {item['name']} with {len(item['detect_data'])} detections")

            if args.debug:
                logger.debug(f"Detection data: {item['detect_data']}")

                logger.debug(f"Adding debug data to image for {item['name']}")
                debug_path = f'{args.output}/debug'
                debug_image = add_debug_data(
                    image_data=original_image.copy(), 
                    detect_data=item['detect_data'],
                )
                item['image']['debug'] = {
                    'path': debug_path,
                    'data': debug_image
                }
                logger.debug(f"Debug data added for {item['name']}")

                logger.debug(f"Saving debug image for {item['name']}")
                save_image(
                    name=item['name'], 
                    image=debug_image, 
                    output_path=debug_path
                )
                logger.debug(f"Debug image saved for {item['name']}")

            logger.info(f"Censoring image {item['name']}")
            censored_image = censor_image(
                image_data=original_image.copy(), 
                detect_data=item['detect_data'], 
                pixel_size=args.pixel_size
            )
            censored_path = f'{args.output}/censored'
            item['image']['censored'] = {
                'data': censored_image,
                'path': censored_path
            }
            logger.info(f"Censorship completed for {item['name']}")

            logger.info(f"Saving censored image for {item['name']}")
            save_image(
                name=item['name'], 
                image=censored_image, 
                output_path=censored_path
            )
            logger.info(f"Censored image saved for {item['name']}")

            item['status'] = 'done'
            logger.info(f"Finished processing file: {item['name']}")
        except Exception as e:
            item['status'] = 'error'
            logger.error(f"Error processing file {path}: {e}")
        finally:
            logger.progress_percent("Overall Progress", data.index(item) + 1, len(data))
    logger.info("Processing completed for all files")

    if args.debug:
        logger.info("Saving debug data")
        save_file_data(data)
        logger.info("Debug data saved")

if __name__ == "__main__":
    args = get_args()
    logger = AppLogger(
        name="app",
        level="DEBUG" if args.debug else "INFO"
    )
    try:
        logger.info("Starting Application...")
        main(args)
    except Exception as e:
        logger.critical(f"Application error: {e}")
    finally:
        logger.info("Application finished.")
