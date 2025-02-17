from PIL import Image
import pytesseract
import os

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='por')
        return text
    except Exception as e:
        return str(e)

def process_images(input_folder='inputs', output_folder='outputs'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f'resultado_{os.path.splitext(filename)[0]}.txt')
            
            extracted_text = extract_text_from_image(input_path)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            print(f'Processado: {filename}')

if __name__ == "__main__":
    process_images()
