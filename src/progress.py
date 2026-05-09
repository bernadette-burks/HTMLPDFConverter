# progress.py
# Author: Bernadette Burks
# Created: May 7, 2026

# Libraries for conversion and loading bar simulation
from tqdm import tqdm
import time

# Loading bar simulation for installation process and conversion process
def loading_bar(task_name):
    for i in tqdm(range(100), desc=task_name, unit="%"):
        time.sleep(0.05)  # Simulate time taken for installation check
