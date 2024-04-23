# Chinese-Sign-Language-Recognition-Model

**Author:** Zixi Zhou  
**GitHub:** [Chinese-Sign-Language-Recognition-Model](https://github.com/zhoucc20210815/Chinese-Sign-Language-Recognition-Model)

## Introduction
This folder contains files for **chinese gesture recognizer** projects developed based on **yolov5** and on **mediapipe** model. 

Due to GitHub's file upload limitations, I couldn't upload all the necessary files for my project. I've provided download links for the missing parts. Alternatively, you can access all of my data, code, and results directly via my Google Drive link: https://drive.google.com/drive/folders/1hEdRvpAsWlwW4Cdv48oc4u8BFTMOJZtG?usp=drive_link.

### data:
- **Dataset for mediapipe folder:** `my_hand_dataset_mediapipe`, contains original image files for 9 Chinese Sign Language signs: "arrive", "food", "you", "good", "give", "I", "can", "sorry", and "thanks". Complete files can be found in the download link.

- **Dataset for yolo5 folder:** `my_hand_dataset_Yolo5`, contains original image files for 4 Chinese Sign Language signs: "arrive", "food", "you", "good", along with their respective JSON annotation files and TXT annotation files. Complete files can be found in the download link.

### aug_data:
- **Augmented images:** `images`, contains augmented images for training YOLOv5. Complete files can be found in the download link.

- **Annotations:** `annotations.csv`,  contains annotation data for each augmented image.

### yolov5:
- **Final model:** `best.pt`, `best2.pt`, `best3.pt` correspond to models trained for 5, 20, and 50 epochs respectively.
  
- **Configuration file:** `Chinese_Gesture_yolo.yaml`, identifies training and validation data and defining classes.

- **Other yolov5 official files:** Complete files can be found in the download link.

### Codes for yolo5:
- **Collect original images for yolo5**: `00_Collect_images_for_yolo5.py`.

- **Image processing and data augmentation:** `01_Image_processing_and_data_augmentation.ipynb`.

- **Munge data into training data and validation data:** `02_munge_data.py`.

- **Training and testing on GPU (Google Colab):** `03_Training_and_Testing.ipynb`.

### Mediapipe_Chinese_Gesture:
- **Collect original images for mediapipe**: `00_Collect_images_for_mediapipe.py`.

- **Training on Mediapipe (Google Colab):** `01_Mediapipe_hand_train.ipynb`.
  
- **Final model:** `gesture_recognizer.task` can be tested in MediaPipe Studio by simply replacing the "Model selections" module with this file. Here is the link: https://mediapipe-studio.webapps.google.com/studio/demo/gesture_recognizer

### Results:
- **Yolo5 complete training results:** `run_results`, contains the complete training results for epochs 5, 20, and 50. Complete files can be found in the download link.
  
- **Demo videos:** `videos`, contains `yolo5_best_epoch50.mp4` and `mediapipe.mp4`.

### DATASHEET
- **Supplementary Explanations for the Dataset:** `DATASHEET.md`
- **Illustration in the DATASHEET:** `image.png`

## Python Version Requirement
All code is built to run on **Python 3.11.8**, Some parts of the code are only applicable for running on **Google Colab** (already annotated in the respective sections). Please ensure your Python environment meets this version requirement.

