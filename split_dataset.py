import os
import shutil
import random

random.seed(0)


def split_data(img_path, txt_path, new_file_path, train_rate, val_rate, test_rate):

    directory = ["/images", "/labels", "/train", "/val", "/test"]

    images_dir = new_file_path + directory[0]
    labels_dir = new_file_path + directory[1]
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    if not os.path.exists(labels_dir):
        os.makedirs(labels_dir)

    for i in range(2, 5):
        if not os.path.exists(images_dir + directory[i]):
            os.makedirs(images_dir + directory[i])
        if not os.path.exists(labels_dir + directory[i]):
            os.makedirs(labels_dir + directory[i])

    all_images = os.listdir(img_path)
    all_labels = os.listdir(txt_path)
    data = list(zip(all_images, all_labels))
    random.shuffle(data)
    shuffle_images, shuffle_labels = zip(*data)
    train_images = shuffle_images[0: int(len(all_images) * train_rate)]
    train_labels = shuffle_labels[0: int(len(all_labels) * train_rate)]
    val_images = shuffle_images[int(len(all_images) * train_rate): int(len(all_images) * (train_rate + val_rate))]
    val_labels = shuffle_labels[int(len(all_labels) * train_rate): int(len(all_labels) * (train_rate + val_rate))]
    test_images = shuffle_images[int(len(all_images) * (train_rate + val_rate)):]
    test_labels = shuffle_labels[int(len(all_labels) * (train_rate + val_rate)):]

    for file in train_images:
        file_prefix = file.split(".")[0]
        origin_img_path = img_path + "/" + file_prefix + ".jpg"
        new_img_path = images_dir + directory[2] + "/" + file_prefix + ".jpg"
        origin_label_path = txt_path + "/" + file_prefix + ".txt"
        new_label_path = labels_dir + directory[2] + "/" + file_prefix + ".txt"
        shutil.copy(origin_img_path, new_img_path)
        shutil.copy(origin_label_path, new_label_path)

    for file in val_images:
        file_prefix = file.split(".")[0]
        origin_img_path = img_path + "/" + file_prefix + ".jpg"
        new_img_path = images_dir + directory[3] + "/" + file_prefix + ".jpg"
        origin_label_path = txt_path + "/" + file_prefix + ".txt"
        new_label_path = labels_dir + directory[3] + "/" + file_prefix + ".txt"
        shutil.copy(origin_img_path, new_img_path)
        shutil.copy(origin_label_path, new_label_path)

    for file in test_images:
        file_prefix = file.split(".")[0]
        origin_img_path = img_path + "/" + file_prefix + ".jpg"
        new_img_path = images_dir + directory[4] + "/" + file_prefix + ".jpg"
        origin_label_path = txt_path + "/" + file_prefix + ".txt"
        new_label_path = labels_dir + directory[4] + "/" + file_prefix + ".txt"
        shutil.copy(origin_img_path, new_img_path)
        shutil.copy(origin_label_path, new_label_path)


if __name__ == '__main__':
    img_path = "/home/temp/images"
    txt_path = "/home/temp/labels"
    new_file_path = "/home/dataset/cat-dog-dataset"
    split_data(img_path, txt_path, new_file_path, 0.8, 0.1, 0.1)