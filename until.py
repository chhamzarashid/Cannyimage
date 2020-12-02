from cv2 import cv2
from matplotlib import pyplot as plt
def canny(path):
    orig_im = cv2.imread(path,0)
    cannyimg = cv2.Canny(orig_im, 100, 200)
   
    cv2.waitKey(0)
    cv2.destroyAllWindows
    plt.subplot(1,2,1),plt.imshow(orig_im,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(cannyimg,cmap = 'gray')
    plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
    plt.show()
def laplacian(path1):
    orig_im = cv2.imread(path1,0)
    laplacianimg =  cv2.Laplacian(orig_im ,cv2.CV_64F)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    plt.subplot(1,2,1),plt.imshow(orig_im,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(laplacianimg,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.show()
def sobel(path):
     orig_im = cv2.imread(path,0)
     sobelx = cv2.Sobel(orig_im,cv2.CV_64F,1,0, ksize=5) 
     sobely = cv2.Sobel(orig_im,cv2.CV_64F,0,1,ksize=5)  
     cv2.waitKey(0)
     cv2.destroyAllWindows
     plt.subplot(2,2,1),plt.imshow(orig_im,cmap = 'gray')
     plt.title('Original'), plt.xticks([]), plt.yticks([])
     plt.subplot(2,2,2),plt.imshow(sobelx,cmap = 'gray')
     plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
     plt.subplot(2,2,3),plt.imshow(sobely,cmap = 'gray')
     plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
     plt.show()
