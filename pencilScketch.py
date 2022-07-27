# Let’s import it to get started with the task
import cv2
import os
# Now the next thing to do is to read the image
image = cv2.imread("C:/Users/anant/OneDrive/Desktop/data/Project/lets_grow_more/ImageToPencilSketch/squirrel.png")
# Reducing the size of the image
# image = cv2.resize(image, (int(image.shape[1]/4), int(image.shape[0]/4)))

# Now after reading the image, we will create a new image by converting the original image to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Now the next step is to invert the new grayscale image
inverted = 255 - gray_image

# Now the next step in the process is to blur the image by using the Gaussian Function in OpenCV
blury_image = cv2.GaussianBlur(inverted, (23, 23), 0)

# Then the final step is to invert the blurred image, then we can easily convert the image into a pencil sketch:
blury_inverted = 255 - blury_image
# cv2.imshow("s", blury_inverted)
pencil_sketech = cv2.divide(gray_image, blury_inverted, scale = 250)

# cv2.imshow("blury_image", blury_image)
# cv2.imshow("inverted", inverted)

# cv2.imshow("gray", gray_image)

# cv2.imshow("jami", image)

cv2.imshow("pencil_sketech", pencil_sketech)
path = os.path.join(os.getcwd(), 'ImageToPencilSketch/' 'pencil sketch.jpg')
# Save images in JPG format
cv2.imwrite(path, pencil_sketech)
cv2.waitKey(0)