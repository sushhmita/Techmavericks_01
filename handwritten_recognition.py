import numpy as np
import pandas as pd
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('A_Z Handwritten Data.csv')

def preprocess_data(data):
    """
    Preprocesses the dataset by detecting and cropping identical borders
    in the handwritten images.
    """
    def detect_identical_borders(vect_image, dim):
        """
        Detects borders where the image data is identical.
        """
        np_image = np.reshape(vect_image, dim)
        height, width = np_image.shape
        tolerance = 100
        # Detect top, bottom, left, and right borders with nearly identical pixel values
        top_border = np.where(~np.all(np.isclose(np_image[0], np_image, atol=tolerance), axis=1))[0][0]
        bottom_border = np.where(~np.all(np.isclose(np_image[height - 1], np_image, atol=tolerance), axis=1))[0][-1]
        left_border = np.where(~np.all(np.isclose(np_image[:, 0], np_image, atol=tolerance), axis=0))[0][0]
        right_border = np.where(~np.all(np.isclose(np_image[:, width - 1], np_image, atol=tolerance), axis=0))[0][-1]
        return [left_border, top_border, right_border, bottom_border]

    # Convert data to numpy array and reshape
    data_array = data.to_numpy()
    matrix = np.reshape(data_array[:, 1:], (data_array.shape[0], 28, 28))
    
    # Detect borders and crop images
    borders = np.apply_along_axis(detect_identical_borders, 1, data_array[:, 1:], (28, 28))
    mean_borders = np.mean(borders, axis=0).astype(int)  # Averaging the border positions across all images
    cropped_matrix = matrix[:, mean_borders[1]:mean_borders[3]+1, mean_borders[0]:mean_borders[2]+1]  # Crop based on averaged borders
    cropped_vectors = np.reshape(cropped_matrix, (cropped_matrix.shape[0], -1))  # Flatten the cropped images
    
    # Reconstruct DataFrame with the processed images
    data2 = np.column_stack((data_array[:, 0], cropped_vectors))
    return pd.DataFrame(data2), mean_borders  # Return data and the mean borders

# Preprocess the data
data2, mean_borders = preprocess_data(data)
X = data2.iloc[:, 1:].values
y = data2.iloc[:, 0].values

# Split data into training and testing sets (simplified as using the same data)
X_train, X_test = X, X
y_train, y_test = y, y

# Standardize the features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the Random Forest Classifier
clf = RandomForestClassifier(n_jobs=-1, random_state=42)
clf.fit(X_train, y_train)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Crop the image using the average borders detected during training
    cropped_gray = gray[mean_borders[1]:mean_borders[3]+1, mean_borders[0]:mean_borders[2]+1]

    # Resize cropped frame to match the input dimensions used in training (if needed)
    resized = cv2.resize(cropped_gray, (mean_borders[3] - mean_borders[1] + 1, mean_borders[2] - mean_borders[0] + 1))

    # Flatten, normalize, and standardize
    flat = resized.flatten() / 255.0
    flat = np.expand_dims(flat, axis=0)
    flat = sc.transform(flat)

    # Predict the letter
    prediction = clf.predict(flat)
    letter = chr(prediction[0] + ord('A'))

    # Display the result on the frame
    cv2.putText(frame, f'Predicted Letter: {letter}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow('Handwritten Alphabet Recognition', frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
