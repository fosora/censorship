# Censorship

## Overview

Censorship is a Python project designed to automatically detect and censor NSFW (Not Safe For Work) content in images. The project uses a pre-trained ONNX model for nude detection and provides both censored and debug outputs for each processed image.

## How It Works

1. The script lists all images in the `files/` directory.
2. Each image is processed by the nude detection model.
3. Detected nude regions are censored and saved to `output/censored/`.
4. Debug images with detection overlays are saved to `output/debug/`.

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
python main.py
```

Check the results in `output/censored/` and `output/debug/`
