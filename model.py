from keras.applications import ResNet50, InceptionV3, Xception, VGG16, VGG19
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import cv2
import os

MODELS = {
    "vgg16": VGG16,
    "vgg19": VGG19,
    "inception": InceptionV3,
    "xception": Xception,
    "resnet": ResNet50
}

image_paths = []
folderpath = 'cats/'


for dirpath, dirnames, filenames in os.walk(folderpath):
    for filename in filenames:
        image_paths.append(os.path.join(dirpath, filename))



for model in MODELS.keys():
    inputShape = (224, 224)
    preprocess = imagenet_utils.preprocess_input

    if model in ("inception", "xception"):
        inputShape = (299, 299)
        preprocess = preprocess_input

    print('[INFO]: Loading {}'.format(MODELS[model]))
    Network = MODELS[model] # to recheck
    model = Network(weights="imagenet")

    for image_path in image_paths:
        print("[INFO]: Loading and preprocessing image...")
        image = load_img(image_path, target_size=inputShape)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = preprocess(image)

        # classify the image
        print("[INFO]: classifying image with {}".format(model))
        preds = model.predict(image)
        P = imagenet_utils.decode_predictions(preds)

        orig = cv2.imread(image_path)
        text_place_col = 10 # начальное положение надписи
        text_place_str = 30
        сounter = 0 # счётчик для добавления подписей на рисунок
        image_num = 0 # счётчик самих изображений
        for (i, (imagenetID, label, prob)) in enumerate(P[0]):
            print(i, (imagenetID, label, prob))
            сounter += 1
            #print('{}. {}: {:.2f}%'.format(i+1, label, prob*100))
            cv2.putText(orig, 'Label: {}, {:.2f}%'.format(label, prob*100), (text_place_col, text_place_str), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            text_place_col += 0 # сдвиг следующей надписи по столбцам
            text_place_str += 20 # сдвиг следующей надписи по строкам
            if сounter == len(MODELS.keys()): # если мы пробежали и проставили вероятности для всех моделей - сохраняем картинку
                cv2.imwrite(folderpath + f'{image_num}_.png', orig)
                image_num += 1



        
        #(imagenetID, label, prob) = P[0][0]
        #print(label, prob)
        #
        #cv2.imshow('Classification: ', orig)
        #cv2.waitKey(0)













