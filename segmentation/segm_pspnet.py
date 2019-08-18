import sys
import os
import keras_segmentation
from tqdm import tqdm






images_for_segmentation = '/Users/user/Desktop/aylifind/example_photos/'
output_images = '/Users/user/Desktop/aylifind/PSPNet/'

for image in tqdm(os.listdir(images_for_segmentation)):

	#model = keras_segmentation.pretrained.pspnet_50_ADE_20K()
	model = keras_segmentation.pretrained.pspnet_101_cityscapes() # load the pretrained model trained on Cityscapes dataset
	#model = keras_segmentation.pretrained.pspnet_101_voc12() # load the pretrained model trained on Pascal VOC 2012 dataset
	out = model.predict_segmentation(
		inp = images_for_segmentation + image,
		out_fname = output_images + image
	)