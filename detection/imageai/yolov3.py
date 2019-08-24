from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()



detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "weights/yolo.h5"))
detector.loadModel()
for image in os.listdir(os.path.join(execution_path, "cats_yolov3")):
    image_path = os.path.join(execution_path, r"cats_yolov3/{}".format(image))
    print(image_path)

#detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "cats_yolov3/42.jpg"), 
#                                            output_image_path=os.path.join(execution_path , "42m.jpg"), 
#                                            minimum_percentage_probability=30)

#for eachObject in detections:
#    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
#    print("--------------------------------")
