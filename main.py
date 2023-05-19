import os
import random
import shutil

# Este script se utilizo para crear las carpetas train y test,
# dividir las imagenes (aleatoriamente) en 80% para train, y 20% para test,
# y moverlas a sus respectivas carpetas y clases.

current_dir = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(current_dir, "dataset")

train_path = os.path.join(current_dir, "train")
test_path = os.path.join(current_dir, "test")

os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

subfolders = [f.name for f in os.scandir(dataset_path) if f.is_dir()]

for subfolder in subfolders:
    os.makedirs(os.path.join(train_path, subfolder), exist_ok=True)
    os.makedirs(os.path.join(test_path, subfolder), exist_ok=True)
    
    images = [f.name for f in os.scandir(os.path.join(dataset_path, subfolder)) if f.is_file()]
    
    random.shuffle(images)
    
    split_index = int(0.8 * len(images))
    
    train_images = images[:split_index]
    test_images = images[split_index:]
    
    for image in train_images:
        src_path = os.path.join(dataset_path, subfolder, image)
        dst_path = os.path.join(train_path, subfolder, image)
        shutil.copy2(src_path, dst_path)
    
    for image in test_images:
        src_path = os.path.join(dataset_path, subfolder, image)
        dst_path = os.path.join(test_path, subfolder, image)
        shutil.copy2(src_path, dst_path)
