import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading

# Global list to hold the paths of the selected files
selected_files = []

def process_video_file(input_file):
    """
    Processes any video file. If the input is MP4, it creates a new,
    re-encoded version with '_converted' appended to the name.
    """
    folder, filename = os.path.split(input_file)
    name, ext = os.path.splitext(filename)

    if ext.lower() == '.mp4':
        output_file = os.path.join(folder, f"{name}_converted.mp4")
    else:
        output_file = os.path.join(folder, f"{name}.mp4")

    try:
        command = ["ffmpeg", "-i", input_file, "-c", "copy", output_file]  # try fast copy first no re-encoding just remux into mp4 way quicker
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"Fast copy failed for {filename}, re-encoding...")
        try:
            command = ["ffmpeg", "-i", input_file, "-c:v", "libx264", "-c:a", "aac", output_file] # fast copy failed streams incompatible fall back to full re-encode with h264/aac
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print(f"ERROR: Complete conversion failure for: {filename}")
            return False
    return True

def select_input_files():
    """Opens a file dialog that defaults to showing all files."""
    global selected_files
    files = filedialog.askopenfilenames(
        title="Select video files",
        filetypes=[("All files", "*.*"), ("Video Files", "*.mp4 *.mkv *.avi *.mov *.webm *.flv")]
    )
    if files:
        selected_files = files
        input_entry.delete(0, tk.END)
        input_entry.insert(0, f"{len(selected_files)} file(s) selected")
        progress_label.config(text="")

def run_conversion_thread():
    success_count = 0
    failure_count = 0
    total_files = len(selected_files)
    
    convert_btn.config(state="disabled")
    browse_btn.config(state="disabled")
    
    for i, file_path in enumerate(selected_files):
        current_filename = os.path.basename(file_path)
        progress_label.config(text=f"Processing {i+1} of {total_files}: {current_filename}")
        
        if process_video_file(file_path):
            success_count += 1
        else:
            failure_count += 1
            
    messagebox.showinfo("Success", f"Conversion complete!\n\nSuccessful: {success_count}\nFailed: {failure_count}")
    
    input_entry.delete(0, tk.END)
    progress_label.config(text="Done!")
    convert_btn.config(state="normal")
    browse_btn.config(state="normal")

def start_conversion():
    if not selected_files:
        messagebox.showwarning("Warning", "Please select one or more files")
        return
    
    conversion_thread = threading.Thread(target=run_conversion_thread)
    conversion_thread.start()

# --- Create GUI ---
root = tk.Tk()
root.title("Video to MP4 Converter")
root.geometry("500x170")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill="both", expand=True)
main_frame.columnconfigure(1, weight=1)

tk.Label(main_frame, text="Input Files:").grid(row=0, column=0, padx=(0, 5), sticky="w")
input_entry = tk.Entry(main_frame)
input_entry.grid(row=0, column=1, sticky="ew")

browse_btn = tk.Button(main_frame, text="Browse...", command=select_input_files)
browse_btn.grid(row=0, column=2, padx=(5, 0))

progress_label = tk.Label(main_frame, text="", fg="navy")
progress_label.grid(row=1, column=1, pady=10, sticky="w")

convert_btn = tk.Button(main_frame, text="Convert to MP4", command=start_conversion, bg="green", fg="white")
convert_btn.grid(row=2, column=1, pady=10)

root.mainloop()
