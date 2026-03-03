Time ↔ Frames GUI

A lightweight Python GUI tool for converting time (hh:mm:ss) to video frame numbers, and vice versa.

This tool is useful in behavioral neuroscience and video analysis workflows where frame indices must be converted to timestamps.

The application provides two functions:

- Time → Frames
- Frames → Time

The GUI is built with Tkinter, so it runs locally without requiring a web browser.


Features

- Convert time → frames
- Convert frames → time
- Supports decimal seconds
- Simple GUI interface
- Lightweight (no external dependencies)


Installation

Clone the repository:

git clone https://github.com/minsikyun-xenopus/timeframes-gui.git
cd timeframes-gui


Create a conda environment:

conda create -n timeframes python=3.10
conda activate timeframes


Install the package:

pip install -e .


Run

After installation:

timeframes-gui


Requirements

Python 3.9+

Tkinter (usually included with Python)

Linux users may need to install Tkinter:

sudo apt install python3-tk


Example

Example conversion:

FPS = 30
Time = 01:00:00

Result:

Frames = 108000


Reverse conversion:

Frames = 108000
FPS = 30

Result:

Time = 01:00:00


Project Structure

timeframes-gui
│
├── pyproject.toml
├── README.md
│
└── src
    └── timeframes_gui
        ├── __init__.py
        └── app.py


Author

Minsik Yun


License

MIT License

