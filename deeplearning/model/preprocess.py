import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocessing(path):
    '''
    Preprocesses the image for the deep learning model
    '''
    # reading the image
    image = cv2.imread(path)

    # converting to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # reducing the image size into 256x256
    im_len = 1024
    dim = (im_len, im_len)
    image = cv2.resize(image, dim,
                        interpolation=cv2.INTER_LINEAR)
    original = image # for debuggin purposes
    
    # applying gaussian filter
    image = cv2.GaussianBlur(image, (3,3), 0)
    
    # segmentation
    ret, image = cv2.threshold(image, 10, 255,
                            cv2.THRESH_BINARY_INV
                             + cv2.THRESH_OTSU)
    
    # finding the biggest contour
    contours, hierarchy = cv2.findContours(image.copy(),
            cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    
    biggest_contour = max(contours, key=cv2.contourArea)
    
    # further noise reduction
    kernel = np.ones((3,3), np.uint8)
    image = cv2.morphologyEx(image,
         cv2.MORPH_OPEN, kernel, iterations=2)

    # drawing a rectangle around the contour
    (x, y, w, h) = cv2.boundingRect(biggest_contour)

    original = cv2.rectangle(original,
            (x,y+h),(x+w,y),
             (0, 255, 125), 2)

    # cropping the image
    original = original[y:y+h, x:x+w]

    # resizing the image into 256x256
    im_len_2 = 256
    dim = (im_len_2, im_len_2)
    original = cv2.resize(original, dim,
                        interpolation=cv2.INTER_LINEAR)
    #print(original.shape)

    return original
    
    
    # displaying the image
    winname = 'preprocess'
    winname2 = 'original'
    
    cv2.namedWindow(winname) # Create a named window
    cv2.moveWindow(winname, 40,30)
    cv2.imshow(winname, image)
    cv2.imshow('original', original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_all_files(root_path):
    '''
    function to get all the image file paths recursively
    ''' 
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

    return all_image_files