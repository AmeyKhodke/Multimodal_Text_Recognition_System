import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

@st.cache_resource
def get_model():
    pass

with st.spinner("loading model....."):
    model = get_model()

st.title('✍️ Handwritten Word Recognition')
st.caption("CNN - BiLSTM Model trained on IAM handwriting dataset")
st.write("Upload the Image of the Handwritten word to see the Model's prediction")

uploaded_file = st.file_uploader("Upload an image ", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_bytes, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Recognizing......."):
        preprocessed = ''
        prediction = ''
        predicted_text = ''
    
    with col2:
        st.subheader("Predicted Text ")
        if predicted_text:
            st.success(predicted_text)
        else:
            st.warning("No text detected, Please upload the image again")
else:
    st.info("Please upload the Handwritten Image...")
