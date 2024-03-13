import tensorflow as tf
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
# from keras.applications import MobileNet
# from keras.preprocessing import image
# from keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np
import io

def predictModel(fileImage):
    model = tf.keras.models.load_model('pothole_3.h5')
    # infer = model.signatures["serving_default"]

    # Convert image format
    # img = Image.open(io.BytesIO(fileImage.read()))
    # img = img.resize((224, 224))
    img_bytes = io.BytesIO(fileImage.read())
    img = image.load_img(img_bytes, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array = preprocess_input(img_array)

    # Classify the image
    predictions = model.predict(img_array)
    print('--> ', predictions)
    # predictions = infer(tf.constant(img_array))

    predicted_class_index = np.argmax(predictions)
    class_labels = ['normal', 'pothole']
    predicted_class_label = class_labels[predicted_class_index]

    # result = decode_predictions(predictions, top=3)[0]
    return predicted_class_label
