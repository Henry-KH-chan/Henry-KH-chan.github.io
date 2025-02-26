# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:39:18 2025

@author: KHChan
"""

import os
import json
import glob

# Define the gallery folder path (adjust as needed)
gallery_folder = 'gallery'  # e.g., "gallery" folder in the current directory

# Define allowed image extensions
allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

# Use glob to find all files in the gallery folder (recursively, if needed)
# For non-recursive, you can use: glob.glob(os.path.join(gallery_folder, '*'))
image_files = glob.glob(os.path.join(gallery_folder, '*'))

# Filter out only the files with allowed image extensions
images = []
for file_path in image_files:
    ext = os.path.splitext(file_path)[1].lower()
    if ext in allowed_extensions:
        # If you want just the src path, store it. You can also add more data here.
        images.append({
            "src": file_path
            "alt": ~
            "caption": ~
        })

# Write the results to a JSON file
output_file = 'gallery.json'
with open(output_file, 'w') as f:
    json.dump(images, f, indent=2)

print(f"Found {len(images)} images. Data written to {output_file}.")