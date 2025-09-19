# Censorship

## Overview

Censorship is a Python project designed to automatically detect and censor NSFW (Not Safe For Work) content in images. The project uses a pre-trained ONNX model for nude detection and provides both censored and debug outputs for each processed image.

## Features

- Automatically scans images for NSFW content.
- Censors detected nude regions using pixelation.
- Generates debug images with detection overlays for analysis.
- Logs progress and errors during processing.
- Supports batch processing of images.

## Requirements

- Python 3.8+
- ONNX Runtime
- OpenCV
- nudenet (>=3.4.2)
- libgl1 (system dependency)

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

or :

```bash
pip install --upgrade "nudenet>=3.4.2";
pip install opencv-python;
```

```bash
sudo apt-get install -y libgl1
```

Place images to be processed in the `files/` directory.
Run the main script:

```bash
source .venv/bin/activate
```

```bash
python main.py
```

### Command Line Arguments

You can also customize parameters, for example:

```bash
python main.py --input my_images --output results --pixel-size 8 --debug --force-process --save-result-json
```

| Argument                   | Default                             | Description                                                                                  |
|----------------------------|-------------------------------------|----------------------------------------------------------------------------------------------|
| `-i`, `--input`            | `files`                             | Input directory containing images to process                                                 |
| `-o`, `--output`           | `output`                            | Output directory to save processed images                                                    |
| `-e`, `--extensions`       | `.jpeg .jpg .png`                   | List of image file extensions to process                                                     |
| `-r`, `--recursive`        | *(flag)*\*                          | Recursively search for images in subdirectories                                              |
| `-p`, `--pixel-size`       | `3`                                 | Pixelation block size for censorship (higher = more pixelated, range: 1-256)                 |
| `-b`, `--blur`             | *(flag)*\*                          | Apply blur effect for censorship instead of pixelation (Not working yet)                     |
| `-d`, `--debug`            | *(flag)*                            | Enable debug mode to save debug images with detection overlays                               |
| `--save-result-json`       | *(flag)*                            | Save the results to a JSON file                                                              |
| `-l`, `--labels`           | FEMALE_GENITALIA and MALE_GENITALIA | List of labels to detect                                                                     |
| `--force-process`          | *(flag)*                            | Force processing of images even when they have no changes                                    |
| `-v`, `--verbose`          | *(flag)*\*                          | Enable verbose output                                                                        |
| `-q`, `--quiet`            | *(flag)*\*                          | Suppress non-error messages                                                                  |
| `--logpath`                | `logs`                              | Folder to the log file                                                                       |
| `--loglevel`               | `INFO`                              | Logging level for the log file (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)             |

> The arguments that contains a \* on it are not working yet and might even be removed. Avoid using it.
