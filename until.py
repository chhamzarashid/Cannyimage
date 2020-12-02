from cv2 import cv2
from matplotlib import pyplot as plt
def canny(path):
    orig_img = cv2.imread(path,0)
    cannyimg = cv2.Canny(orig_img, 100, 200)
    plt.subplot(1,2,1),plt.imshow(orig_img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(cannyimg,cmap = 'gray')
    plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
    plt.show()
def laplacian(path):
    orig_img = cv2.imread(path,0)
    laplacianimg =cv2.Laplacian(orig_img,cv2.CV_64F,ksize=5)
    plt.subplot(1,2,1),plt.imshow(orig_img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(laplacianimg,cmap = 'gray')
    plt.title('laplacian Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    
def sobel(path):
     orig_img = cv2.imread(path,0)
     sobelx = cv2.Sobel(orig_img,cv2.CV_64F,1,0, ksize=5) 
     sobely = cv2.Sobel(orig_img,cv2.CV_64F,0,1,ksize=5)  
     plt.subplot(2,2,1),plt.imshow(orig_img,cmap = 'gray')
     plt.title('Original'), plt.xticks([]), plt.yticks([])
     plt.subplot(2,2,2),plt.imshow(sobelx,cmap = 'gray')
     plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
     plt.subplot(2,2,3),plt.imshow(sobely,cmap = 'gray')
     plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
     plt.show()
