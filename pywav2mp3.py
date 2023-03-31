import tkinter as tk
from os import path
from pydub import AudioSegment
import glob

def convert_file():
    
    # Ask user which file to convert
    file_to_convert = filename_entry.get()

    # Check if file exists
    if not path.isfile(file_to_convert):
        result_label.config(text="File not found.")
    else:
        # Set output filename
        dst = file_to_convert.replace(".wav", ".mp3")

        # Convert wav to mp3
        sound = AudioSegment.from_wav(file_to_convert)
        sound.export(dst, format="mp3")

        result_label.config(text="File converted successfully.")

    # Clear filename entry
    filename_entry.delete(0, tk.END)

root = tk.Tk()
root.title("WAV to MP3 Converter")
root.geometry("300x300")
root.configure(bg="black")

# Create a label to display available files for conversion
file_label = tk.Label(root, text="Available files for conversion:", fg="green", bg="black")
file_label.pack()

# Scan directory for wav files
wav_files = glob.glob("*.wav")

# Create a label for each wav file and pack it
for file in wav_files:
    file_label = tk.Label(root, text=file, fg="green", bg="black")
    file_label.pack()

# Filename label and entry
filename_label = tk.Label(root, text="Enter the filename you want to convert:")
filename_label.config(fg="green", bg="black")
filename_label.pack()

filename_entry = tk.Entry(root, width=30)
filename_entry.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_file)
convert_button.pack()

# Available files label
files_label = tk.Label(root)
files_label.config(fg="green", bg="black")
files_label.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.config(fg="green", bg="black")
result_label.pack()

# Start the GUI
root.mainloop()