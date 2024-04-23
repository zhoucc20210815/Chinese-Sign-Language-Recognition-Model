# The code in this notebook is sourced from Week 4 in-class notebook! 
# I made minor adjustments to adapt it for my custom dataset. 
# The source code link is: https://git.arts.ac.uk/tbroad/AI-4-Media-23-24/tree/main/Week-4-Sensing-bodies
import os
import cv2

# Directory to save the dataset
IMG_DIR = './data/my_hand_dataset_mediapipe'

# Number of classes and frames per class
NUM_OF_CLASSES = 9
NUM_OF_FRAMES = 200

# Class names
class_names = ['you', 'food', 'arrive', 'I', 'can', 'give', 'good', 'sorry' ,'thank']

# Create the directory if it doesn't exist
if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)

# Video capture object
cam = cv2.VideoCapture(0)

# Loop through each class
for i, class_name in enumerate(class_names):
    # Create a folder for the class
    class_dir = os.path.join(IMG_DIR, class_name)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    # Prompt user to start collecting data for the class
    print('Press "y" to start collecting data for class: {}'.format(class_name))

    # Wait for user input to start capturing frames
    while True:
        success, frame = cam.read() 
        if success and cv2.waitKey(25) == ord('y'):
            j = 5
            while j > 0:
                print('Start collecting in {}'.format(j))
                cv2.waitKey(1000)
                j -= 1
            break
        cv2.imshow('frame', frame)

    # Collect frames for the class
    print('Collecting...')
    counter = 0
    while counter < NUM_OF_FRAMES:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
        counter += 1

# Print message after collecting data for all classes
print('Collected image data for {} different classes'.format(NUM_OF_CLASSES))

# Release camera object 
cam.release() 
# Destroy all windows 
cv2.destroyAllWindows()
