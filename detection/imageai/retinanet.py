from imageai.Detection import ObjectDetection
import os
from skimage.io import imread, imsave

execution_path = os.getcwd()
input_folder = '/Users/user/Desktop/aylifind/detection/cats_original/'
output_folder = '/Users/user/Desktop/aylifind/detection/retinanet_e/'


detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "weights/retinanet.h5"))
detector.loadModel()


for image in os.listdir(input_folder):
    print(input_folder + image)
    print(output_folder + image)
    custom = detector.CustomObjects(cat=True)
    detections = detector.detectCustomObjectsFromImage(input_image=input_folder + image, 
                                                       output_image_path=output_folder + image,
                                                       custom_objects=custom, 
                                                       minimum_percentage_probability=70)

    for eachObject in detections:
        try:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            print("--------------------------------")
            print(type(eachObject["box_points"]))
            x1 = eachObject["box_points"][0]
            y1 = eachObject["box_points"][1]
            x2 = eachObject["box_points"][2]
            y2 = eachObject["box_points"][3]
            img = imread(input_folder + image)
            imsave(output_folder+'{}'.format(image), img[y1:y2, x1:x2])
        except:
            continue

