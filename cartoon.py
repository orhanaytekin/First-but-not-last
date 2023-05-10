
import sys
import cv2
import numpy as np
import random

def cartoonize(img, k):
    temp_img = img
    
    img = cv2.imread(img)
    path_for_the_first = "cartoon.jpg"
    path_for_the_second = "shades.jpg"
    list_of_images = []
    list_of_images.append(img)
    # Defining input data for clustering

    data = np.float32(img).reshape((-1,3))

        # Defining criteria
    criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        # Applying cv2.kmeans function
    _, label, center = cv2.kmeans(
        data, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    # print(center)
        # Reshape the output data to the size of input image
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    list_of_images.append(result)
    # cv2.imshow("result", result)
    cv2.imwrite(path_for_the_first,result)
    # Convert the input image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Perform adaptive threshold
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)
    list_of_images.append(edges)
    cv2.imwrite(path_for_the_second,edges)
    # cv2.imshow('edges', edges)
    # Smooth the result
    blurred = cv2.medianBlur(result, 3)
    # Combine the result and edges to get final cartoon effect
    cartoon = cv2.bitwise_and(blurred, blurred)
    list_of_paths = [temp_img,path_for_the_first,path_for_the_second]
    return list_of_paths

print("--------------------------------")
img = cv2.imread('image.png')
list_of_images = cartoonize("new_trial/image.png", 8)
input1= input("Which one would you like?\n1.) Show me the original image.\n"+
              "2.) Cartoonized imaged with color.\n3.) Cartoonized image with edges.\nIf you want to quit, press q or Q.\n(1, 2, 3, q or Q.): ")

while True:
    if input1 == "1":
        cv2.imshow("cartoon",list_of_images[0])
        cv2.imwrite("cartoon.jpg",list_of_images[0])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif input1 == "2":
        cv2.imshow("cartoon",list_of_images[1])
        cv2.imwrite("cartoon.jpg",list_of_images[1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif input1 == "3":
        cv2.imshow("cartoon",list_of_images[2])
        cv2.imwrite("cartoon.jpg",list_of_images[2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif input1.lower() == 'q':
        sys.exit(1)
    else:
        print("Invalid input type, please respond with either 1, 2, 3, q or Q.")
    input1= input("Which one would you like?\n1.) Show me the original image.\n"+
              "2.) Cartoonized imaged with color.\n3.) Cartoonized image with edges.\nIf you want to quit, press q or Q.\n(1, 2, 3, q or Q.): ")
