import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("lenagray.jpg",0)
# um besser ergebniss sehen zu können begrenzen wir Histogramm
def findMinMaxMat(mat):
    min=255
    max=0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j]>max:
                max=mat[i,j]
            if mat[i,j]<min:
                min=mat[i,j]
    return (min,max)
def LimitHistogram(img):
    (Imin,Imax)=findMinMaxMat(img)
    (Omin,Omax)=(80,140)
    outImage = np.zeros((img.shape),dtype="uint8")
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            outImage[i,j]=((((Omax-Omin)/(Imax-Imin))*(img[i,j]-Imin))+Omin)
    return outImage
img=LimitHistogram(img)
def equaliz(img):
    equ=cv2.equalizeHist(img)
    hist_Orginal=cv2.calcHist ([img],[0],None,[256],[0,255])
    hist_equ = cv2.calcHist([equ], [0], None, [256], [0,255])
    plt.figure()
    plt.subplot(221) , plt.imshow(img,"gray") , plt.title("Orginal"),
    plt.xticks([]),plt.yticks([])
    plt.subplot(222), plt.imshow(equ, "gray"), plt.title("Ergebniss"),
    plt.xticks([]), plt.yticks([])
    plt.subplot(223) ,plt.plot(hist_Orginal) ,plt.title("Histogramm"),
    plt.xlim(0, 255)
    plt.subplot(224) , plt.plot (hist_equ) , plt.title("angepasst") ,plt.xlim(0,255),
    plt.yticks([])
    plt.show()
equaliz(img)


