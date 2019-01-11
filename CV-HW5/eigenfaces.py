# Author: Alperen Kantarcı
# In order to run this file run following command
# python eigenfaces.py
# You need to have Face_database folder in the same directory with the script
# If folder name is different change the path name in main function it is relative path

import os, os.path
import cv2
import numpy as np
import math
from numpy import random
from scipy import linalg
from matplotlib import pyplot as plt

# This function prints the given images together with mean image
def print_eigenfaces(mean,D,H,W,title,cols=5,scale=1):
    n = np.shape(D)[0]
    rows = int(math.ceil((n+1+0.0)/cols))
    fig = plt.figure(1,figsize=[scale*20.0/H*W,scale*20.0/cols*rows],dpi=300)
    fig.canvas.set_window_title(title)
    for i in range(n):
        ax = plt.subplot(rows,cols,i+1)
        ax.set_title('Eigenface {}' .format(i+1),fontsize=8)
        ax.imshow(np.reshape(D[i,:],[H,W]), cmap = plt.get_cmap("gray"))
        plt.axis('off')
    # Plot mean image
    ax = plt.subplot(rows,cols,n+3)
    ax.set_title('Mean face' ,fontsize=8)
    ax.imshow(np.reshape(mean,[H,W]), cmap = plt.get_cmap("gray"))
    plt.axis('off')
    plt.show()

# This function prints test image and reconstructed image
def print_reconstructed(D,target,H,W,title,cols=5,scale=1):
    n = np.shape(D)[0]
    rows = int(math.ceil((n+1+0.0)/cols))
    fig = plt.figure(1,figsize=[scale*20.0/H*W,scale*20.0/cols*rows],dpi=300)
    fig.canvas.set_window_title(title)
    for i in range(n):
        ax = plt.subplot(rows,cols,i+1)
        ax.set_title('Target image {}' .format(i+1),fontsize=8)
        ax.imshow(np.reshape(target[i],[H,W]), cmap = plt.get_cmap("gray"))
        plt.axis('off')
    # Plot target image
    ax = plt.subplot(rows,cols,n+3)
    ax.set_title('Reconstructed image with {} eigenvectors'.format(cols) ,fontsize=8)
    ax.imshow(np.reshape(D,[H,W]), cmap = plt.get_cmap("gray"))
    plt.axis('off')
    plt.show()

# Using ecludian distance find the closest image weights in the database
def calculateDistance(database,test_img):
	closest_distance = float("inf")
	closest_index = -1
	for index,weights in enumerate(database):
		weight_sum = 0
		for i,j in enumerate(weights):
			weight_sum += np.sqrt(np.abs(test_img[i]-j)**2)
		if weight_sum < closest_distance:
			closest_distance = weight_sum
			closest_index = index
	return database[closest_index]

def main():
	imgs = []
	path = "Face_database/"
	valid_images = [".jpg",".tif",".png",".tga"]
	# (a) Load images from the Face_database directory.
	for f in os.listdir(path):
	    ext = os.path.splitext(f)[1]
	    if ext.lower() not in valid_images:
	        continue
	    imgs.append(os.path.join(path,f))
	imgs.sort()

	# (a) Convert all the images to numpy array
	images = [cv2.imread(x,cv2.IMREAD_GRAYSCALE) for x in imgs]
	orj_w,orj_h = images[0].shape
	faces = np.empty(shape=[1, images[0].shape[0]*images[0].shape[1]])

	# (a) Convert them to vectors and stack them to one matrix horizontally
	images = [np.reshape(a,(1,-1)) for a in images ]
	for i in images:
		faces = np.vstack((faces,i))
	faces = np.delete(faces, (0), axis=0)

	# (b) Find mean face
	mean_image = np.mean(images, axis=0)

	# (b) Substract mean face so find Z vector
	arr_norm = np.zeros([len(images), orj_w*orj_h])
	arr_norm = faces - mean_image

	# (c) In here A*A.T is used for fast calculation of SVD
	# Here we calculate len(faces)xlen(faces) dimension instead covariance matrix
	S = np.matmul(arr_norm,arr_norm.T)
	u, s, vh = np.linalg.svd(S, full_matrices=True)
	# Sort eigenvalues descending
	idx = s.argsort()[::-1]
	s = s[idx]
	u = u[:,idx]
	# (c) Get eigen vectors and print them
	eigenvectors = np.matmul(u.T,arr_norm)
	num_eigfaces = 5
	print_eigenfaces(mean_image,eigenvectors[:num_eigfaces,:],orj_w,orj_h,"Part A Eigen Faces")

	# PART B of the project
	# Calculate each image weights for desired number of eigenvectors
	weight_database = np.matmul(arr_norm,eigenvectors[:num_eigfaces,:].T)
	# (a) Get random image to recognize and add gaussian noise
	img_id = np.random.randint(len(images),size=1)
	test_face = faces[img_id]
	# (b) Transform to basis B
	smoothed_face = cv2.GaussianBlur(test_face,(3,3),0.0125,0,cv2.BORDER_DEFAULT).reshape((1,-1))
	smoothed_face -= mean_image

	# (c) Calculate weights of the face
	face_weight = np.matmul(eigenvectors[:num_eigfaces,:],smoothed_face.T)
	# (d) Find the closest weights in database
	closest_weights = calculateDistance(weight_database,face_weight)
	# (e) Reconstruct the image with given eigenvectors and their weights
	reconstructed = mean_image + np.matmul(closest_weights.T,eigenvectors[:num_eigfaces,:])
	print_reconstructed(reconstructed,test_face,orj_w,orj_h,"Part B Face Recognition")

if __name__ == '__main__':
	main()
