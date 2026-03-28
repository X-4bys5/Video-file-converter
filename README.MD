# Video-Converter

A desktop app i made to batch convert video files to mp4. i needed to convert a bunch of mkv files and doing them one by one was annoying as well as many website had a limit of upto 1gb maximum but with this i have unlimited gb so i built this.

it tries a fast copy first (no re-encoding, way faster), and if that fails it falls back to full re-encoding with h264/aac.

## how it works
```
- pick one or multiple video files
- it tries to copy the streams directly into mp4 first
- if that fails it re-encodes with ffmpeg
- shows progress while its running so the ui doesnt freeze
```
## stack

- python + tkinter for the gui
- ffmpeg for the actual conversion (called via subprocess)
- pyinstaller to build the exe

## requirements

you need ffmpeg installed and in your PATH, get it from https://ffmpeg.org/download.html

## run it
```
git clone https://github.com/X-4bys5/Video-file-converter.git
cd Video-file-converter
python convertmany.py
```
or just download the exe from the dist folder if you dont want to deal with python

## known issues
```
- no progress bar showing percentage, just shows which file its on
- if ffmpeg isnt in PATH it crashes with a confusing error
- doesnt show estimated time remaining
```
