import os
import random
from PIL import Image

def rotate_images(folder, percentage):
    files = os.listdir(folder)
    image_files = [file for file in files if file.lower().endswith(('.jpg'))]

    num_rotate = int(len(image_files) * percentage / 100)

    selected_files = random.sample(image_files, num_rotate)

    for file in selected_files:
        image_path = os.path.join(folder, file)
        img = Image.open(image_path)

        rotated_img = img.rotate(180)

        new_image_path = os.path.join(folder, file)
        rotated_img.save(new_image_path)

        print(f"Rotated {file} as {new_image_path}")

# For now there is a 30% to flip an image
folder_path = "Test_images"
rotation_percentage = 30

rotate_images(folder_path, rotation_percentage)
