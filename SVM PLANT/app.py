import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
healthy_images_paths = [
    "path_to_local_image1.jpg",  
    "path_to_local_image2.jpg",   
    "path_to_local_image3.jpg"    
]
diseased_images_paths = [
    "path_to_local_image4.jpg"   
     
]
def load_images(paths, label):
    images = []
    labels = []
    for path in paths:
        try:
            img = cv2.imread(path)  
            if img is not None:
                img = cv2.resize(img, (128, 128))  
                images.append(img)
                labels.append(label)
            else:
                print(f"Failed to load image from {path}")
        except Exception as e:
            print(f"Error loading image from {path}: {e}")
    return images, labels
healthy_images, healthy_labels = load_images(healthy_images_paths, 'healthy')
diseased_images, diseased_labels = load_images(diseased_images_paths, 'diseased')
X = np.array(healthy_images + diseased_images)
y = np.array(healthy_labels + diseased_labels)
if X.size == 0:
    print("No images were loaded. Please check the paths or files.")
else:
    X, y = shuffle(X, y, random_state=42)
    X = X / 255.0
    X_flat = X.reshape(X.shape[0], -1)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X_flat, y_encoded, test_size=0.2, random_state=42)
    model = SVC(kernel='linear', random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))