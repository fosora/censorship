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
source /workspaces/censorship/.venv/bin/activate
```

```bash
python main.py
```

### Command Line Arguments

You can also customize parameters, for example:

```bash
python main.py --input my_images --output results --pixel-size 8 --debug
```

| Argument              | Default   | Description                                                       |
|-----------------------|-----------|-------------------------------------------------------------------|
| `-i`, `--input`       | `files`   | Input directory containing images to process                      |
| `-o`, `--output`      | `output`  | Output directory to save processed images                         |
| `-p`, `--pixel-size`  | `3`       | Pixelation block size for censorship (higher = more pixelated)    |
| `-d`, `--debug`       | *(flag)*  | Enable debug mode to save debug images with detection overlays    |
