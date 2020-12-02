from cv2 import cv2
from matplotlib import pyplot as plt
def cannyimg():
    img = cv2.imread('1.jpg',0)
    canny = cv2.Canny(img,50,100)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(canny,cmap = 'gray')
    plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
    plt.show()

