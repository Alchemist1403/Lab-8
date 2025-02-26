import cv2


def image_centering(image):
    img = cv2.imread(image)
    y,x = img.shape[:2]
    
    if x % 2 != 0:
        x -= 1

    if y % 2 != 0:
        y -= 1

    center_x = int(x/2)
    center_y = int(y/2)

    center = img[center_y - 200:center_y + 200, center_x - 200:center_x + 200]
    cv2.imshow('image', center)
    cv2.imwrite("small_cat.jpg",center)


if __name__ == '__main__':
    image_centering('variant-8.jpg')

cv2.waitKey(0)
cv2.destroyAllWindows()