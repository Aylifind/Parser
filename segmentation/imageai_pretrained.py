import glob
from imageai.Detection import ObjectDetection
from imageai.Prediction import ImagePrediction
import os


"""
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

# Load model
model_path = '/Users/user/Desktop/segmentation/object_detection/h5/yolo-tiny.h5'

detector.setModelPath(model_path)
detector.loadModel()

input_images_path = 'original/*'
output_images_path = '/Users/user/Desktop/segmentation/object_detection/yolo_tiny/'
custom_objects = detector.CustomObjects(dog=False, 
                                        cat=True, 
                                        bird=False, 
                                        cow=False, 
                                        elephant=False, 
                                        bear=False)

# Iterate through folder of images
count = 0
for f in glob.glob(input_images_path):
    # Set output file path
    output_path = output_images_path + 'result_' + str(count) + '.jpg'
    
    # Detect
    print('Detecting...', output_path)
    detector.detectCustomObjectsFromImage(input_image=f, output_image_path=output_path, custom_objects=custom_objects, minimum_percentage_probability=40)
    count += 1
"""



from imageai.Prediction import ImagePrediction
import os


model_path = '/Users/user/Desktop/segmentation/object_detection/h5/squeezenet_weights_tf_dim_ordering_tf_kernels.h5'

multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsSqueezeNet()
multiple_prediction.setModelPath(model_path)
multiple_prediction.loadModel()

all_images_array = []

all_files = os.listdir('original/')

for each_file in all_files:
    if (each_file.endswith(".jpg") or each_file.endswith(".png")):
        # /Users/user/Desktop/segmentation/object_detection/original
        all_images_array.append('/Users/user/Desktop/segmentation/object_detection/original/'+each_file)


print(all_images_array)
results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)

print(results_array)
"""
for each_result in results_array:
    predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions[index] , " : " , percentage_probabilities[index])
    print("-----------------------")

"""
# Образец вывода:
# {'predictions': ['kelpie', 'Chihuahua', 'skunk', 'schipperke', 'toy_terrier'], 
# 'percentage_probabilities': [21.48558795452118, 12.273447960615158, 12.240554392337799, 5.857811123132706, 5.407411232590675]}




    
