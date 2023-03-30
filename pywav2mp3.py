from os import path
from pydub import AudioSegment
import glob

while True:
    # Scan directory for wav files
    wav_files = glob.glob("*.wav")

    # Display available files for conversion
    print("Available files for conversion:")
    for file in wav_files:
        print(file)

    # Ask user which file to convert
    file_to_convert = input("Enter the filename you want to convert: ")

    # Check if file exists
    if not path.isfile(file_to_convert):
        print("File not found.")
    else:
        # Set output filename
        dst = file_to_convert.replace(".wav", ".mp3")

        # Convert wav to mp3
        sound = AudioSegment.from_wav(file_to_convert)
        sound.export(dst, format="mp3")

        print("File converted successfully.")

    # Ask user if they want to convert another file
    choice = input("Do you want to convert another file? (y/n)")
    if choice.lower() != "y":
        break

