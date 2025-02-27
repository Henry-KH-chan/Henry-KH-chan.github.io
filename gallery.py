import os
import json
import glob

# Define the gallery folder path (adjust as needed)
gallery_folder = 'gallery'  # Folder where your images are stored

# Define allowed image extensions
allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

# Get all files in the gallery folder (non-recursive)
image_files = glob.glob(os.path.join(gallery_folder, '*'))

# Filter the files and create a list of dictionaries with "src", "alt", and "caption" keys
images = []
for file_path in image_files:
    ext = os.path.splitext(file_path)[1].lower()
    if ext in allowed_extensions:
        # Normalize the path to use forward slashes
        normalized_path = file_path.replace(os.sep, '/')
        images.append({
            "src": normalized_path,
            "alt": "",
            "caption": ""
        })

# Write the results to a JSON file
output_file = 'gallery.json'
with open(output_file, 'w') as f:
    json.dump(images, f, indent=2)

print(f"Found {len(images)} images. Data written to {output_file}.")
