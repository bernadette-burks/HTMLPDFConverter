# installer.py
# Author: Bernadette Burks
# Created: May 7, 2026

# Libraries for installing pyhtml2pdf
import subprocess 
import sys

# Subprocess for installing pyhtml2pdf (if not already installed) without showing output in the terminal
def install_pyhtml2pdf():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyhtml2pdf"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
