# Video-file-converter
A lightweight Python desktop application that automates the conversion of various video formats into web-standard MP4 files.


## KEY FEATURES

1. Batch Processing: Select and queue multiple files at once using a native file explorer.
2. Smart Encoding Logic: Attempts a "Fast Copy" first to save time; automatically switches to full re-encoding (H.264/AAC) only if the copy fails.
3. Non-Blocking UI: Utilizes Python’s threading library to ensure the GUI remains responsive while FFmpeg handles heavy processing in the background.
4. Cross-Platform Compatibility: Handles .mkv, .avi, .mov, .webm, and more.


## TECH STACK

Language: Python 3.x 
GUI Framework: Tkinter 
Core Engine: FFmpeg (via subprocess) 
Packaging: PyInstaller (for .exe generation)


## PREREQUISITES
This tool is a wrapper for FFmpeg. You must have FFmpeg installed and added to your System PATH for the conversion to work.


## SETUP
1. Clone & install
"git clone <your-repo-url>"
"python -m venv venv"
"venv\Scripts\activate"

## Run locally
2. python convertmany.py

## OR ELSE
- GO TO DIST/ DOWNLOAD .exe and run convertmany.exe
