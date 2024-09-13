import cv2
import pytesseract
from PIL import Image

# Configure the path to the tesseract executable
# Update the path based on your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image):
    """
    Perform OCR on the given image and return the extracted text.
    """
    # Convert the image to a format suitable for pytesseract
    pil_image = Image.fromarray(image)
    text = pytesseract.image_to_string(pil_image)
    return text

def main():
    print("Live OCR Application")
    print("Press 'q' to quit.")
    
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Perform OCR on the captured frame
        text = perform_ocr(frame)
        
        # Display the captured frame
        cv2.imshow('Live OCR', frame)
        
        # Display the extracted text
        print("Extracted Text:", text)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
