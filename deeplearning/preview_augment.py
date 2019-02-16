from keras.preprocessing.image import (ImageDataGenerator,
                                    array_to_img,
                                    img_to_array,
                                    load_img)

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')


img = load_img('new_leaf_data/dried_diseased/leaf-image7.jpg')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 256, 256)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 256, 256, 3)
print(x.shape)

i = 0
for batch in datagen.flow(x, batch_size=1,
                            save_to_dir='preview',
                            save_prefix='dried-diseased',
                            save_format='jpg'):
    i += 1
    if i >20:
        break