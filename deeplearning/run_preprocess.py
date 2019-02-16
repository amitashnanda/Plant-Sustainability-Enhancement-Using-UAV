import cv2
import os
import preprocess

# root folder
root_path = "raw_leaf_data/"

all_image_files = preprocess.get_all_files(root_path)

for f,idx in zip(all_image_files, range(len(all_image_files))):
    t = preprocess.preprocessing(f)
    target_class = f.split('\\')[0].split('/')[1]
    print(target_class)
    cv2.imwrite(os.path.join('new_leaf_data', target_class, "leaf-image"+str(idx))+'.jpg', t)
    print('saved', os.path.join('new_leaf_data', target_class, "leaf-image"+str(idx))+'.jpg')
