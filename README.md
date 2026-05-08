# HTML to PDF Converter :card_index_dividers:
Utility script that converts webpages to PDF documents using Python

Author: Bernadette Burks  
Created: May 7, 2026

ABOUT THIS SCRIPT ---
This script installs a program that converts a website to PDF using the pyhtml2pdf library.
This script also contains a sample conversion of NASA.gov Images page to PDF, saving it to a specified location on the user's desktop.
Script includes error handling, timeout option for rendering JavaScript elements, and feedback if the module is not found.

REQUIREMENTS ---  
pyhtml2pdf  
tqdm

HOW TO USE ---
To use the program, simply change the info contained in the converter.convert() function to convert a different website or save to a different location.
Sample PDF will save to the user's Downloads folder, but you can change the path to save it anywhere on your computer. Just make sure to include the .pdf extension at the end of the file name!

To run this script, simply execute it in a Python environment!
