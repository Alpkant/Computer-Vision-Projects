import cv2
import numpy as np
from matplotlib import pyplot as plt
import os,os.path

# Author: Alperen Kantarcı
# In order to run this file run following command
# python lucaskanade.py
# You need to have traffic_sequence folder in the same directory with the script 
# If folder name is different change the path name in main function it is relative path

imgs = []
path = "traffic_sequence/"
valid_images = [".jpg",".jpeg",".png",".tga"]

def calc_derivatives(old_frame, new_frame):
    # Get derivatives with kernels  
    kernel_x = np.fliplr(0.25 * np.array(([-1, 1], [-1, 1])))
    kernel_y = 0.25 * np.array(([-1, -1], [1, 1]))
    kernel_t = 0.25 * np.array(([1,0],[0,1]))
    # Get convolutions of the kernels so that calculate derivatives
    Ix = cv2.filter2D(old_frame, -1, kernel_x) + cv2.filter2D(new_frame, -1, kernel_x)
    Iy = cv2.filter2D(old_frame, -1, kernel_y) + cv2.filter2D(new_frame, -1, kernel_y)
    It = cv2.filter2D(old_frame, -1, kernel_t) + cv2.filter2D(new_frame, -1, -kernel_t)
    return (Ix, Iy, It)

def lucas_kanade(old_frame, new_frame,window):
    # Get derivatives between two images
    Ix, Iy, It = calc_derivatives(old_frame, new_frame)
    # Denominator
    denom = cv2.filter2D(Ix**2, -1, window)*cv2.filter2D(Iy**2, -1, window) - cv2.filter2D((Ix*Iy), -1, window)**2
    denom[denom == 0] = np.inf
    # Calculate u and v values using window with pi pixels
    u = (-cv2.filter2D(Iy**2, -1, window)*cv2.filter2D(Ix*It, -1, window) + cv2.filter2D(Ix*Iy, -1, window)*cv2.filter2D(Iy*It, -1, window)) / denom
    v = (cv2.filter2D(Ix*It, -1, window)*cv2.filter2D(Ix*Iy, -1, window) - cv2.filter2D(Ix**2, -1, window)*cv2.filter2D(Iy*It, -1, window)) / denom

    return (u, v)

# Get images inside of the directory
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(os.path.join(path,f))
# Make sequences in order
# Convert all the images to numpy array with grayscale
imgs.sort()
images = [cv2.imread(x,cv2.IMREAD_GRAYSCALE) for x in imgs]

#For all the sequences
for T in range(len(images)-1):
    plt.figure(1)
    plt.clf()
    #Get two images
    old_frame = np.float32(images[T])
    new_frame = np.float32(images[T+1])

    # Window size of the lucas kanade algorithm
    pixel_width= 25
    # Calculate optical flow using two different algorithms
    u, v = lucas_kanade(old_frame, new_frame, np.ones((pixel_width, pixel_width)))
    
    # Create grid for display
    x = np.arange(0, old_frame.shape[1], 1)
    y = np.arange(0, old_frame.shape[0], 1)
    x, y = np.meshgrid(x, y)

    # Display
    plt.title("Optical flow of the Hamburg Taxi")
    plt.axis('off')
    plt.imshow(old_frame, cmap='gray', interpolation='bicubic')
    
    step = 8
    # Create vector field and give the motion to the vector field to visualize 
    plt.quiver(x[::step, ::step], y[::step, ::step],u[::step, ::step], v[::step, ::step],edgecolor="k",color='r', pivot='middle', headwidth=4, headlength=4,scale = 50)
    plt.pause(0.3)
    plt.draw()