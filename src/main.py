# main.py
# Author: Bernadette Burks
# Created: May 7, 2026

from installer import install_pyhtml2pdf
from progress import loading_bar

# Loading bar for installation
loading_bar("Checking installation")

# Install pyhtml2pdf
install_pyhtml2pdf()

try:
    from converter_utils import convert_website_to_pdf
except ImportError:
    import sys
    print("Error: converter module could not be loaded.")
    sys.exit(1)

# Loading bar for conversion
loading_bar("Converting to PDF")

# Convert website to PDF
output_file = convert_website_to_pdf(
    "https://www.nasa.gov/images/",
    "nasa_sample.pdf"
)

print(f"PDF successfully created at: {output_file}")