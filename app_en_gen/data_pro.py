# python3.7
# -*- coding: utf-8 -*-
# @Author : listen
# @Time   :

import os
import json
import shutil

def train_lable():
    # test
    with open(r"F:\fix_bug\data\text_renderer_en\char_spacing_compact\test_data\labels.json", "r", encoding="utf-8") as f:
        label = json.load(f)
        labels = label["labels"]

        with open("./test_label.txt", "w", encoding="utf-8") as label_file:
            for item in labels.items():
                text = item[1].replace("\n", "")
                t = "images/" + item[0] + ".jpg\t" + text + "\n"
                label_file.write(t)
        # labels = label["labels"].keys()
        print(labels)
        pass

    # with open("", "a", encoding="utf-8") as f:
    #     pass
if __name__ == "__main__":
    train_lable()
    # test_image()
    # test_lable(bg=6)
    pass
