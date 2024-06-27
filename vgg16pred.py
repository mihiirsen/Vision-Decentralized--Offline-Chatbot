import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('models/vgg16.h5')

def get_high_confidence_class(predictions, threshold=0.9):
    class_index = np.argmax(predictions)  
    if predictions[0][class_index] >= threshold:
        return class_index
    else:
        return None

def predict(image):
    img = image.convert('RGB')  
    img = img.resize((224, 224))  
    img_array = np.array(img)  
    img_array = img_array / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  

    predictions = model.predict(img_array)

    return predictions

#0 normal 1 bacterial 2 viral
def reverse_encoding(high_confidence_class):
    if high_confidence_class is None:
        return "NOTHING"
    if high_confidence_class==0:
        return "NORMAL LUNG CHEST CASE"
    if high_confidence_class==1:
        return "BACTERIAL LUNG CHEST CASE"
    if high_confidence_class==2:
        return "VIRAL LUNG CHEST CASE"

def predictive_label(image):
    val=predict(image)
    high_confidence_class = get_high_confidence_class(val, threshold=0.9)
    return (reverse_encoding(high_confidence_class))
# print(predictive_label("uploads/xraytest.jpeg"))