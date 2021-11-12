# python3.7
# -*- coding: utf-8 -*-
# @Author : listen
# @Time   :
import os
import json
import shutil

def test_lable(bg=1):
    # test
    with open("bg{}_gen/output/test_data/labels.json".format(bg), "r", encoding="utf-8") as f:
        label = json.load(f)
        labels = label["labels"]
        for key in range(0, 10):
            labels["{}0000000{}".format(bg, key)] = labels.pop("00000000{}".format(key))
        for key in range(10, 100):
            labels["{}000000{}".format(bg, key)] = labels.pop("0000000{}".format(key))
        for key in range(100, 1000):
            labels["{}00000{}".format(bg, key)] = labels.pop("000000{}".format(key))

        with open("data/test_label.txt", "a", encoding="utf-8") as label_file:
            for item in labels.items():
                text = item[1].replace("\n", "")
                t = "train_data/image/" + item[0] + ".jpg\t" + text + "\n"
                label_file.write(t)
        # labels = label["labels"].keys()
        print(labels)
        pass

    # with open("", "a", encoding="utf-8") as f:
    #     pass


def test_image(bg=6):
    path = "./bg{}_gen/output/test_data/images/".format(bg)
    image_list = os.listdir(path)
    for file_obj in image_list:
        file_path = os.path.join(path, file_obj)
        new_name = os.path.join("./data/test_images", str(bg) + file_obj[1:])
        shutil.copyfile(file_path, new_name)

def train_lable(bg=6):
    # test
    with open("bg{}_gen/output/train_data/labels.json".format(bg), "r", encoding="utf-8") as f:
        label = json.load(f)
        labels = label["labels"]
        for key in range(0, 10):
            labels["{}0000000{}".format(bg, key)] = labels.pop("00000000{}".format(key))
        for key in range(10, 100):
            labels["{}000000{}".format(bg, key)] = labels.pop("0000000{}".format(key))
        for key in range(100, 1000):
            labels["{}00000{}".format(bg, key)] = labels.pop("000000{}".format(key))
        for key in range(1000, 10000):
            labels["{}0000{}".format(bg, key)] = labels.pop("00000{}".format(key))
        for key in range(10000, label["num-samples"]):
            labels["{}000{}".format(bg, key)] = labels.pop("0000{}".format(key))

        with open("data/train_label.txt", "a", encoding="utf-8") as label_file:
            for item in labels.items():
                text = item[1].replace("\n", "")
                t = "train_data/train_images/" + item[0] + ".jpg\t" + text + "\n"
                label_file.write(t)
        # labels = label["labels"].keys()
        print(labels)
        pass

def train_image(bg=1):
    path = "./bg{}_gen/output/train_data/images/".format(bg)
    image_list = os.listdir(path)
    for file_obj in image_list:
        file_path = os.path.join(path, file_obj)
        new_name = os.path.join("./data/train_images", str(bg) + file_obj[1:])
        shutil.copyfile(file_path, new_name)

    # with open("", "a", encoding="utf-8") as f:
    #     pass
if __name__ == "__main__":
    for i in range(3, 7):
        train_image(i)
    # test_image()
    # test_lable(bg=6)
    pass
