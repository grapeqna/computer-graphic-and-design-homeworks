import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalization(img_path):
    
    org_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) #отваряме картинката чернобяла

    #взимаме хистограмата на оригиналната картинка
    org_hist, _ = np.histogram(org_img, bins=256, range=(0, 256))

    #new_hist променливата е новата хистограма, която ще пресметнем (Hsum)
    new_hist = np.zeros_like(org_hist)
    new_hist[0] = org_hist[0] #Po(new_hist) = Po(hist) (пикселът горе в ляво- първият)

    #използвайки метод 1 пресмятаме Hsum
    for i in range(1, len(org_hist)):
        new_hist[i] = new_hist[i - 1] + org_hist[i]

    #пресмятаме пикселите с най-ниски стойности и ги изваждаме, за да може цялата хистограма да започне от 0
    #след това прилагаме новопресметнатите пиксели върху новата картинка
    #демек картинката вече е с тази нова хистограма, запазваме картинката
    map = ((new_hist - new_hist.min()) / (org_img.size - 1) * 255).astype('uint8')
    new_img = map[org_img]
    cv2.imwrite("./fin_img.png", new_img)

    #пресмятаме хистограмата на новата(финална) картинка, за да може да се покаже като графика, а не като масив
    fin_hist, _ = np.histogram(new_img, bins=256, range=(0, 256))

    #чрез библиотеката plot визуализираме 2те картинки и 2те хистограми
    plt.figure(figsize=(15, 5))

    #показвам първо оригиналната картинка (в grayscale)
    plt.subplot(1, 4, 1)
    plt.imshow(org_img, cmap='gray')
    plt.title('Input image')

    #после показвам "оправената" картинка (също в grayscale)
    plt.subplot(1, 4, 2)
    plt.imshow(new_img, cmap='gray')
    plt.title('Final image')

    #хистограмата на оригиналната картинк
    plt.subplot(1, 4, 3)
    plt.plot(org_hist, color='orange')
    plt.title('Histogram of input image')

    #и накрая изравнената хистограма
    plt.subplot(1, 4, 4)
    plt.plot(fin_hist, color='purple')
    plt.title('Histogram of final image')

    plt.tight_layout() #подсигуряваме че картинките не се припокриват
    plt.show()

equalization('img.png')
#няма общо със задачата и обясненията, но много се забавлявах с цветовете на графиките и заглавията