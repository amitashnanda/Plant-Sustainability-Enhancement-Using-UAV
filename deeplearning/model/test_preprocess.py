# import necessary packages
import os
import random
import cv2
from preprocess import preprocessing

# selecting a random image for testing
root_path = "raw_leaf_data/"
all_image_files = []
for fold in os.listdir(root_path):
    all_image_files = (all_image_files +
                       sorted([os.path.join(root_path, fold, file)
                                for file in os.listdir(
                                    os.path.join(root_path, fold)
                                    )
                                ]
                            )
                        )

r_no = random.randint(0, len(all_image_files)-1)
test_image = all_image_files[r_no]
print('displaying', test_image)
random_save = preprocessing(test_image)
cv2.imwrite('test.jpg', random_save)