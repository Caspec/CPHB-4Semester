import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os

# Create histograms over all images we download and two super histograms
def histogram_saver(arr, superhist):
    blue_channels_hist = []
    green_channels_hist = []
    red_channels_hist = []
    for imagename in arr:
        image = cv2.imread(imagename)
        cv2.imshow("image", image)
        chans = cv2.split(image)
        colors = ("b", "g", "r")
        plt.figure()
        plt.title(imagename + "' - BGR Color Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.axis([0, 256, 0, 6000])
        features = []
        for (chan, color) in zip(chans, colors):
            # create a histogram for the current channel and
            # concatenate the resulting histograms for each
            # channel
            hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
            if color == 'b':
               blue_channels_hist.append(hist.T[0][:])
            elif color == 'g':
               green_channels_hist.append(hist.T[0][:])
            elif color == 'r':
               red_channels_hist.append(hist.T[0][:])
            features.extend(hist)
            # plot the histogram
            plt.plot(hist, color = color)
            plt.xlim([0, 256])
    
        plt.savefig('./data/histogram/' + os.path.basename(imagename))
        
    # Super histogram
    b = np.mean(blue_channels_hist, axis=0)
    g = np.mean(green_channels_hist, axis=0)
    r = np.mean(red_channels_hist, axis=0)
    plt.figure()
    plt.title(superhist + "' - BGR Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.axis([0, 256, 0, 6000])
    plt.plot(b, color='b')
    plt.plot(g, color='g')
    plt.plot(r, color='r')
    plt.xlim([0, 256])
    plt.savefig('./data/histogram/' + os.path.basename(superhist))
   
# Create histogram on a specific image with different axis than the others  
def oneimage(imagename):
    image = cv2.imread(imagename)
    cv2.imshow("image", image)
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(imagename + "' - One Image")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.axis([20, 30, 0, 4000])
    features = []
    for (chan, color) in zip(chans, colors):
        # create a histogram for the current channel and
        # concatenate the resulting histograms for each
        # channel
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)
        # plot the histogram
        plt.plot(hist, color = color)
        plt.xlim([20, 30])
  
        plt.savefig('./data/histogram/' + os.path.basename(imagename)) 