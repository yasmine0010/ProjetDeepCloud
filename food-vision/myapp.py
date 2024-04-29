import streamlit as st
import tensorflow as tf
import os
from utils import load_and_prep_image, classes_and_models

# Obtenez le chemin absolu du répertoire actuel
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Charger le modèle TensorFlow depuis un chemin relatif dans le conteneur Docker
MODEL_PATH = os.path.join(CURRENT_DIR, "efficientnet_model_1_10_classes.h5")
MODEL = tf.keras.models.load_model(MODEL_PATH)

#### SideBar ####

st.sidebar.title("What's Food Vision ?")
st.sidebar.write("""
FoodVision is an end-to-end **CNN Image Classification Model** which identifies the food in your image. 

It can identify over 100 different food classes

It is based upon a pre-trained Image Classification Model that comes with Keras and then retrained on the infamous **Food101 Dataset**.

**Accuracy :** **`85%`**

**Model :** **`EfficientNetB1`**

**Dataset :** **`Food101`**
""")

# Streamlit code
st.title("🍔🍟🍗 Welcome to Food Vision 🍞🍖🍕")
st.header("Identify what's in your food photos! 📸")

def make_prediction(image, model, class_names):
    image = load_and_prep_image(image)
    image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
    preds = model.predict(image)
    pred_class = class_names[tf.argmax(preds[0])]
    pred_conf = tf.reduce_max(preds[0])
    return image, pred_class, pred_conf

CLASSES = classes_and_models["model_1"]["classes"]

uploaded_file = st.file_uploader(label="Upload an image of food",
                                 type=["png", "jpeg", "jpg"])

if not uploaded_file:
    st.warning("Please upload an image.")
    st.stop()
else:
    uploaded_image = uploaded_file.read()
    st.image(uploaded_image, use_column_width=True)
    pred_button = st.button("Predict")

if pred_button:
    image, pred_class, pred_conf = make_prediction(uploaded_image, model=MODEL, class_names=CLASSES)
    st.write(f"Prediction: {pred_class}, Confidence: {pred_conf:.3f}")
