import cv2

def resize_image(arr):
    for img_str in arr:
        image = cv2.imread(img_str)
        resize_image = cv2.resize(image, (800,600), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(img_str, resize_image)

        
