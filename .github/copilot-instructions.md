# Workspace Instructions for `censorship`

This project is a Python-based image censorship tool that detects nude content and produces censored output images.

## What to know first

- The main application entrypoint is `main.py`.
- Core logic is organized under `src/` into feature areas:
  - `src/args.py` and argument helper modules for CLI parsing
  - `src/file_management/` for input discovery and result saving
  - `src/image_edition/` for image loading, censoring, and saving
  - `src/nsfw_detection/` for model-based nude detection
  - `src/debug_mode/` for logging and debug image support
- The project uses `requirements.txt` for Python dependencies.
- There is no dedicated automated test suite in the repository today.

## Recommended setup

- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```
- The project expects Python 3.8+.
- The README describes a `source .venv/bin/activate` workflow; respect the virtual environment if present.

## How to run

Use the CLI via `python main.py`.

Example:

```bash
python main.py --input files --output output --pixel-size 8 --debug --save-result-json
```

The most important runtime behavior:

- `--input` defaults to `files`
- `--output` defaults to `output`
- `--pixel-size` controls censorship strength and must be between 1 and 256
- `--debug` writes debug overlay images
- `--save-result-json` writes JSON metadata
- `--force-process` is used to process images even when no nude content is found

## Agent guidance for modifications

- Prioritize changes inside `src/` unless the user explicitly asks to add new project structure.
- Keep CLI behavior consistent with existing `argparse` helpers under `src/args.py`.
- If adding features, avoid changing the entrypoint or runtime model semantics without a clear user request.
- The repository currently has no test directory; if tests are requested, propose adding `tests/` at the repo root and use a standard runner such as `pytest`.
- Do not assume additional dataset or model training support is required; the current scope is inference/processing with pre-trained ONNX models.

## When editing documentation

- Prefer updating `README.md` with user-facing usage changes.
- Keep this instructions file focused on agent workflows and project-specific context.
- Link to `README.md` rather than duplicating long usage examples.
