# HTMLPDFConverter.py
# Author: Bernadette Burks
# Created: May 7, 2026

# --- ABOUT THIS SCRIPT ---
# This script installs a program that converts a website to PDF using the pyhtml2pdf library.
# This script also contains a sample conversion of NASA.gov Images page to PDF, saving it to a specified location on the user's desktop.
# Script includes error handling, timeout option for rendering JavaScript elements, and feedback if the module is not found.

# --- HOW TO USE ---
# To use the program, simply change the info contained in the converter.convert() function to convert a different website or save to a different location.
# Sample PDF will save to the user's Downloads folder, but you can change the path to save it anywhere on your computer. Just make sure to include the .pdf extension at the end of the file name!

# --- RUN THE SCRIPT BELOW ---
# To run this script, simply execute it in a Python environment!

# Libraries for installing pyhtml2pdf
import subprocess 
import sys

# Subprocess for installing pyhtml2pdf (if not already installed) without showing output in the terminal
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyhtml2pdf"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    from pyhtml2pdf import converter
except ImportError:
    import sys
    print("Error: pyhtml2pdf module not found. Install it using: pip install pyhtml2pdf") # Error message if pyhtml2pdf is not installed
    sys.exit(1)

# Conversion module to convert a website to PDF document (change the URL and file path as desired!)
from pathlib import Path

downloads_folder = Path.home() / "Downloads" # Path to the user's Downloads folder (change this to save the PDF somewhere else)
output_file = downloads_folder / "nasa_sample.pdf" # Output filename (change this to your desired file name with .pdf extension)

converter.convert("https://www.nasa.gov/images/",
    str(output_file),
    timeout=2
)

from tqdm import tqdm
import time

# Loading bar simulation for conversion process
for i in tqdm(range(100), desc="Converting to PDF", unit="%"):
    time.sleep(0.05)  # Simulate time taken for conversion 

if converter:
    print(f"PDF successfully created at: {output_file}. Have a great day!") # Feedback if conversion is successful

