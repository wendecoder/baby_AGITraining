import numpy as np
from hyperon import *
# from tensorflow.keras.applications import EfficientNetB0
from keras.preprocessing import image
from keras.applications.efficientnet import preprocess_input, decode_predictions
# from tensorflow.keras.models import load_model
from keras.models import load_model
import io
from pathlib import Path

# model = load_model('best_model.h5')

SC_label_names = {
    0: 'MEL(Melanoma (Highly cancerous))',    # Melanoma (Highly cancerous)
    1: '(Melanocytic nevus (Not cancerous))',     # Melanocytic nevus (Not cancerous)
    2: 'BCC(Basal cell carcinoma (Cancerous))',    # Basal cell carcinoma (Cancerous)
    3: 'AK(Actinic keratosis (Precancerous))',     # Actinic keratosis (Precancerous)
    4: 'BKL(Benign keratosis-like lesions (Not cancerous))',    # Benign keratosis-like lesions (Not cancerous)
    5: 'DF(Dermatofibroma (Usually not cancerous))',     # Dermatofibroma (Usually not cancerous)
    6: 'VASC(Vascular lesions (Varies in cancerousness))',   # Vascular lesions (Varies in cancerousness)
    7: 'SCC(Squamous cell carcinoma (Cancerous))',    # Squamous cell carcinoma (Cancerous)
    8: 'UNK(Unknown (Uncertain cancerousness))'     # Unknown (Uncertain cancerousness)
}
def detect_skin_cancer(metta: MeTTa, *args):

    pwd = Path(__file__).parent

    for atom in args:
      img_path = f"{pwd}/{(atom)}"

    model = load_model(f'{pwd}/best_model.h5')

    IMAGE_SIZE = [331, 331]
    

    # Load and preprocess the image
    with open(img_path, 'rb') as imageFile:
        image_data = imageFile.read()

    img = image.load_img(io.BytesIO(image_data), target_size=(331, 331))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    print("this is image array: ", img_array)
    img_array = img_array.reshape((1, img_array.shape[0], img_array.shape[1], img_array.shape[2]))

    # Print the shape of the image tensor
    print("Shape of the preprocessed image:", img_array.shape)
    
    # Make predictions
    preds = model.predict(img_array)
    
    prediction_idx = np.argmax(preds, axis=-1)
    print(prediction_idx[0])
    labeled_prediction = SC_label_names[prediction_idx[0]]    
    labeled_prediction_atom = metta.parse_single(labeled_prediction)
    return [ValueAtom(labeled_prediction_atom)]

# Example usage
# image_path = 'skinlession.jpg'
# detect_skin_cancer(image_path)
