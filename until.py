from cv2 import cv2
from matplotlib import pyplot as plt
def canny(path):
    orig_im = cv2.imread(path,0)
    cannyimg = cv2.Canny(orig_im, 100, 200)
   
    cv2.waitKey(0)
    cv2.destroyAllWindows
    plt.subplot(121),plt.imshow(orig_im,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cannyimg,cmap = 'gray')
    plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
    plt.show()

