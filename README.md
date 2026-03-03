TIME ↔ FRAMES GUI

A simple Python GUI tool for converting time (hh:mm:ss) to video frame numbers and vice versa.

---

DESCRIPTION

This tool provides a graphical interface for converting between:

* Time (hours, minutes, seconds)
* Video frame numbers

It is useful for video analysis workflows in behavioral neuroscience
and other experiments where frame indices must be converted to timestamps.

The application includes two main functions:

• Time → Frames
• Frames → Time

The GUI is built with Tkinter and runs locally without requiring
a web browser or external dependencies.

---

FEATURES

* Convert time to frame number
* Convert frame number to time
* Supports decimal seconds
* Simple graphical user interface
* Lightweight (no external dependencies)

---

INSTALLATION

1. Clone the repository

git clone https://github.com/minsikyun-xenopus/timeframes-gui.git
cd timeframes-gui

2. Create a conda environment

conda create -n timeframes python=3.10
conda activate timeframes

3. Install the package

pip install -e .

---

RUNNING THE PROGRAM

After installation, run:

timeframes-gui

---

REQUIREMENTS

Python 3.9 or newer

Tkinter (usually included with Python)

Linux users may need to install Tkinter manually:

sudo apt install python3-tk

---

EXAMPLE

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

---

PROJECT STRUCTURE

timeframes-gui

pyproject.toml
README.md

src/
timeframes_gui/
**init**.py
app.py

---

AUTHOR

Minsik Yun
Postdoctoral Researcher
Johns Hopkins University

Research interests:

* Insect neuroethology
* Behavioral analysis
* Neural circuit mechanisms

---

LICENSE

MIT License


