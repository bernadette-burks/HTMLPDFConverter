# converter_utils.py
# Author: Bernadette Burks
# Created: May 7, 2026

# Conversion module to convert a website to PDF document (change the URL and file path as desired!)
from pathlib import Path
from pyhtml2pdf import converter

def convert_website_to_pdf(url, filename):
    downloads_folder = Path.home() / "Downloads" # Path to the user's Downloads folder (change this to save the PDF somewhere else)
    output_file = downloads_folder / filename # Output filename (change this to your desired file name with .pdf extension)

    converter.convert(url,
        str(output_file),
        timeout=2
    )

    return output_file