from PIL import Image
import pytesseract

# Path to tesseract executable
# On Windows, you need to specify the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# On Linux and macOS, it's usually available directly via the PATH environment variable.

# Load an image(path to users text image)
image_path = r'C:\Users\admin\Desktop\txtimg.jpg'
img = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the text
print(text)

