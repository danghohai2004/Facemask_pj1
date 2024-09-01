import cv2
import os

def check_img_size(path):
    count_wrong_size = 0
    input_folder = path
    target_size = (224, 224)
    print("Check size .....")

    for f_name in os.listdir(input_folder):
        if f_name.endswith('.jpg') or f_name.endswith('.png'):
            img_path = os.path.join(input_folder, f_name)
            img = cv2.imread(img_path)
            height, width, _ = img.shape
            if (width, height) != target_size:
                count_wrong_size += 1

    if count_wrong_size == 0:
        print("Check size successfully!, all photos are the correct size of 224x224")
    else:
        print("number of photos of the wrong size: ",count_wrong_size)

def change_size_224(inpath, outpath):
    input_folder = inpath
    output_folder = outpath
    target_size = (224, 224)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print("Change to size 224x224 .....")

    for f_name in os.listdir(input_folder):
        if f_name.endswith('.jpg') or f_name.endswith('.png'):
            img_path = os.path.join(input_folder, f_name)
            img = cv2.imread(img_path)
            resized_img = cv2.resize(img, target_size)
            output_path = os.path.join(output_folder, f_name)
            cv2.imwrite(output_path, resized_img)

    print("Change to size successfully!")

def data_normalization(inpath, outpath):
    if not os.path.exists(inpath):
        os.makedirs(outpath)

    for filename in os.listdir(inpath):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(inpath, filename)
            img = cv2.imread(img_path)
            normalized_img = img.astype('float32') / 255.0
            output_path = os.path.join(outpath, filename)
            cv2.imwrite(output_path, (normalized_img * 255).astype('uint8'))



if __name__ == "__main__":
