import cv2
import os
import time

def process_images(input_folder, output_folder, target_size=(224, 224), normalize=False):
    count_wrong_size = 0

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("Check Size .....")

    for f_name in os.listdir(input_folder):
        if f_name.endswith('.jpg') or f_name.endswith('.png'):
            img_path = os.path.join(input_folder, f_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f"Error reading {f_name}, skipping.")
                continue

            height, width = img.shape[:2]

            if (width, height) != target_size:
                count_wrong_size += 1
                img = cv2.resize(img, target_size)

            if normalize:
                img = img.astype('float32') / 255.0

            img_to_save = (img * 255).astype('uint8') if normalize else img

            output_path = os.path.join(output_folder, f_name)
            cv2.imwrite(output_path, img_to_save)

    if count_wrong_size > 0:
        print(f"Number of photos with wrong size: {count_wrong_size}, and resized to {target_size}")
    else:
        print("All photos are the correct size of", target_size)

    if normalize:
        print("Implement standardization .....")

    print("Processing Complete!")


if __name__ == "__main__":
    input_folder = 'Dataset/with_mask'
    output_folder = 'Dataset/with_mask'
    process_images(input_folder, output_folder, target_size=(224, 224), normalize=True)
