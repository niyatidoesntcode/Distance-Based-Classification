import os
import cv2
import numpy as np

def check_libraries():
    try:
        import cv2, numpy, sklearn
        print("Libraries are installed.")
    except ImportError as e:
        print(f"Missing: {e.name}")
        exit(1)

def check_files():
    files = ["Plaksha_Faculty.jpg", "Dr_Shashi_Tharoor.jpg", "haarcascade_frontalface_default.xml"]
    for file in files:
        if not os.path.exists(file):
            print(f"Missing: {file}")
            exit(1)
    print("All files are present.")

def check_images():
    images = ["Plaksha_Faculty.jpg", "Dr_Shashi_Tharoor.jpg"]
    for img in images:
        if cv2.imread(img) is None:
            print(f"Cannot load: {img}")
            exit(1)
    print("All images load correctly.")

if __name__ == "__main__":
    check_libraries()
    check_files()
    check_images()
    print("All checks passed.")
