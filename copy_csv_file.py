import shutil
import os

# Define the source and destination paths
source_file = "artifacts/raw.csv"
destination_folder = "notebook/data/"

# Ensure the destination folder exists, create it if necessary
os.makedirs(destination_folder, exist_ok=True)

# Copy the file from the source to the destination
shutil.copyfile(source_file, os.path.join(destination_folder, "raw.csv"))