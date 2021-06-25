## PRE REQUISITE:####################################
# In conda or cmd: pip install streamlit
# To run the py code: streamlit run prod_recog.py
#####################################################

## Import Libraries
import streamlit as st
import cv2
import numpy as np
from skimage import color
from skimage import io

st.image("header.png")
## trying categories
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
model_selction = st.radio("Select category",('Automotive','Tools & Hardware','Home & Pets','Sports & Recreation','Outdoor Living'))
src="https://www.canadiantire.ca/en/hot-deals.html?adlocation=HP_ASPOT_CanadaDaySuperSale_21326"

## File upload button
file = st.file_uploader(" ", type=["jpg", "png"])

## 2 Columns
col1, col2 = st.beta_columns([4,4])

#=============================================================================
# Image Recognition
#=============================================================================

# Load the trained model
import tensorflow as tf
model = tf.keras.models.load_model('PR_model2.h5')

if file is None:
    st.text("Please upload an image file")
else:
    with col1:
        img = io.imread(file)
        st.image(img, width=300)
        im_gray = color.rgb2gray(img) # converting to grayscale
        img = cv2.resize(im_gray, (28, 28)) # converting to IMG_SIZE 90,90
        img = np.array(img).reshape(-1, 28, 28, 1)
        prediction = model.predict(img)
    
    with col2: 
        st.write("Image detected:")
        max = np.max(prediction)
        st.write(prediction)
        
        if prediction[0:,0] == max :
            st.markdown("__FLOOR MATS & LINERS__")
            st.write("Confidence: ", max)
            st.write("Click this [link](https://www.canadiantire.ca/en/search-results.html?q=FLOOR%20MATS%20%26%20LINERS) to view Floor Mats and Liners products")
        elif prediction[0:,1] == max :
            st.markdown("__BRAKE TOOLS__")
            st.write("Confidence: ", max)
            st.write("Click this [link](https://www.canadiantire.ca/en/automotive/loan-a-tool/ac-brake-tools.html) to view Brake Tools products")
        elif prediction[0:,2] == max :
            st.markdown("__WHEEL__")
            st.write("Confidence: ", max)
            st.write("Click this [link](https://www.canadiantire.ca/en/automotive/trailers-towing-accessories/trailer-tires-wheels-tubes.html) to view Wheel products")
        elif prediction[0:,3] == max :
            st.markdown("__TIRE__")
            st.write("Confidence: ", max)
            st.write("Click this [link](https://www.canadiantire.ca/en/automotive/tires-wheels/tires.html) to view Tire products")
        elif prediction[0:,4] == max:
            st.markdown("__MUFFLER__")
            st.write("Confidence: ", max)
            st.write("Click this [link](https://www.canadiantire.ca/en/automotive/auto-parts/emission-exhaust-systems/mufflers.html) to view Muffler products")
        elif prediction[0:,5] == max:
            st.markdown("__SPORTS BATTERY__")
            st.write("Confidence: ", max)
            st.write("Click this [link](https://www.canadiantire.ca/en/search-results.html?q=SPORTS%20BATTERY) to view Sports Battery products")
        else:
            st.write("Unable to detect. Please load another image.")

## iframe for candaian tire app
st.components.v1.iframe(src, scrolling=True)


st.image("footer.png")

#=============================================================================
