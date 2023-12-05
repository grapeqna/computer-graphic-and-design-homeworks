import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def custom_filter_func(image_path, output_path, custom_filter, offset, scale):
    img = np.array(Image.open(image_path))
    height, width, channels = img.shape

    filtered = np.zeros_like(img, dtype=np.float32)

    for i in range(channels):
        for x in range(1, height - 1):
            for y in range(1, width - 1):
                result = (
                    custom_filter[0, 0] * img[x - 1, y - 1, i] +
                    custom_filter[0, 1] * img[x - 1, y, i] +
                    custom_filter[0, 2] * img[x - 1, y + 1, i] +
                    custom_filter[1, 0] * img[x, y - 1, i] +
                    custom_filter[1, 1] * img[x, y, i] +
                    custom_filter[1, 2] * img[x, y + 1, i] +
                    custom_filter[2, 0] * img[x + 1, y - 1, i] +
                    custom_filter[2, 1] * img[x + 1, y, i] +
                    custom_filter[2, 2] * img[x + 1, y + 1, i]
                ) / scale + offset

                filtered[x, y, i] = np.clip(result, 0, 255)

    filtered = filtered.astype(np.uint8)
    Image.fromarray(filtered).save(output_path)
    plot_images(img, filtered)

def plot_images(original, filtered):

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(filtered)
    axes[1].set_title('Filtered Image')
    axes[1].axis('off')
    plt.show()

if __name__ == "__main__":
    
    input_path = "hamster.jpg" #img.jpg e po golqma i bavno zarezhdat filtrit , no i s neq gi testvah
    output_path = "filtered_image.jpg"

    custom_filter = np.array([
     [0, -1, 0],
     [-1, 5, -1],
     [0, -1, 0]
    ])

    offset = 0
    scale = 1  

    custom_filter_func(input_path, output_path, custom_filter, offset, scale)

    #blur
    # custom_filter = np.array([
    #     [2, 2, 2],
    #     [2, 3, 2],
    #     [2, 2, 2]
    # ])

    # offset = 0 
    # scale = 19 

    #inverted
    #  custom_filter = np.array([
    #     [0, 0, 0],
    #     [0, -1, 0],
    #     [0, 0, 0]
    # ])

    # offset = 255
    # scale = 1  

    #emboss
    # custom_filter = np.array([
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, -1]
    # ])

    # offset = 128
    # scale = 1  

    #sharpen
    # custom_filter = np.array([
    #     [0, -1, 0],
    #     [-1, 5, -1],
    #     [0, -1, 0]
    # ])

    # offset = 0
    # scale = 1   
