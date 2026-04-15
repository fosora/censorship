from src.image_data import ImageData
from src.args import get_args
from src.debug_mode.debug import add_debug_data
from src.debug_mode.log import AppLogger
from src.file_management.files import get_files, save_file_data
from src.image_edition.image import get_image, save_image, censor_image
from src.nsfw_detection.nude_detection import detect_nude

def main(args):
    logger = AppLogger(
        name="main",
        log_path=args.output if args.output else args.logpath,
        level=
            "DEBUG" if args.debug else 
            args.logfile_level if args.logfile_level else 
            "INFO"
    )

    logger.info("Fetching files to process")
    files = get_files(args.input, args.extensions, args.recursive)
    if len(files) == 0:
        logger.warning("No files found to process.")
        return
    logger.info(f"Found {len(files)} files to process")

    logger.info("Loading file data")
    image_data = [ImageData(file) for file in files]
    logger.info(f"Loaded data for {len(image_data)} files")

    logger.info("Starting processing of files")
    for image in image_data:
        logger.info(f"Processing file: {image.name}")
        try:
            logger.info(f"Loading original image for {image.name}")
            image.start()
            original_image = get_image(image.path)
            image.set_image('original', original_image, image.path)
            logger.info(f"Image loaded for {image.name}")

            logger.info(f"Detecting nude content in {image.name}")
            detect_data = detect_nude(image.path)
            image.add_detection(detect_data)
            logger.info(f"Detection completed for {image.name}")

            if not detect_data and not args.force_process:
                logger.info(f"No nude content detected in {image.name}, skipping censorship")
                image.finish()
                continue

            if args.debug:
                logger.debug(f"Adding debug data to image for {image.name}")
                debug_path = f'{args.output}/debug'
                debug_image = add_debug_data(
                    image_data=original_image.copy(), 
                    detect_data=detect_data,
                )
                image.set_image(
                    'debug', 
                    debug_image, 
                    f'{debug_path}/{image.name}'
                )
                logger.debug(f"Debug data added for {image.name}")

                logger.debug(f"Saving debug image for {image.name}")
                save_image(
                    name=image.name, 
                    image=debug_image, 
                    output_path=debug_path
                )
                logger.debug(f"Debug image saved for {image.name}")

            logger.info(f"Censoring image {image.name}")
            
            censored_image = censor_image(
                image_data=original_image.copy(), 
                detect_data=detect_data, 
                pixel_size=args.pixel_size
            )
            censored_path = f'{args.output}/censored'
            image.set_image(
                'censored', 
                censored_image, 
                f'{censored_path}/{image.name}'
            )
            logger.info(f"Censorship completed for {image.name}")

            logger.info(f"Saving censored image for {image.name}")
            save_image(
                name=image.name, 
                image=censored_image, 
                output_path=censored_path
            )
            logger.info(f"Censored image saved for {image.name}")

            image.finish()
            logger.info(f"Finished processing file: {image.name}")
        except Exception as e:
            image.error(str(e))
            logger.error(f"Error processing file {image.path}: {e}")
        finally:
            logger.progress_percent("Overall Progress", image_data.index(image) + 1, len(image_data))
    logger.info("Processing completed for all files")

    if args.debug or args.save_result_json:
        logger.info("Saving debug data to JSON")
        save_file_data(image_data, args.output)
        logger.info("Debug data saved to JSON")

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
