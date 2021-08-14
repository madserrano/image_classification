## PRE REQUISITE:#########################################
# In conda or cmd: pip install streamlit
# To run the py code: streamlit run prod_recog.py
# Changes:
# 10-July-2021 - Line 109 changed subcategory_link to link
#              - Cleaned uneccessary lines 
###########################################################

## Import Libraries
import streamlit as st
import cv2
import numpy as np
from skimage import color
from skimage import io
import pandas as pd
import tensorflow as tf


def model_id_find(radio_sel):
    mod_id=0
    if radio_sel == 'Automotive':
        mod_id = 0
    elif radio_sel == 'Tools & Hardware':
        mod_id = 1
    elif radio_sel == 'Home & Pets':
        mod_id = 2
    elif radio_sel == 'Sports & Recreation':
        mod_id = 3
    elif radio_sel == 'Outdoor Living':
        mod_id = 4
    return mod_id


def mod_select(id):
    model_name = 'PR_model_'+str(id)+'.h5'
    return tf.keras.models.load_model(model_name, compile = False)


# trying to fetch link using datasource file
def category_pos_fetch(model_out,vmax):
    col_id=0
    for row in model_out:
        for i in range(len(row)):
            if row[i] == vmax:
                col_id = i
    return col_id

# loading datasource for link fetching
ds = pd.read_csv('datasource.csv',index_col=0)

# loading all model files for faster access, switch to mod_select function if model size too high and comment below lines
#model_0 = tf.keras.models.load_model('PR_model_0.h5')
#model_1 = tf.keras.models.load_model('PR_model_1.h5')
#model_2 = tf.keras.models.load_model('PR_model_2.h5')
#model_3 = tf.keras.models.load_model('PR_model_3.h5')
#model_4 = tf.keras.models.load_model('PR_model_4.h5')

st.image("header.png")

## radio button for categories
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
model_selection_button = st.radio("Select category",('Automotive','Tools & Hardware','Home & Pets','Sports & Recreation','Outdoor Living'))
#src="https://www.canadiantire.ca/en/hot-deals.html?adlocation=HP_ASPOT_CanadaDaySuperSale_21326"

## File upload button
file = st.file_uploader(" ", type=["jpg", "png"])

## 2 Columns
col1, col2 = st.beta_columns([4,4])

#=============================================================================
# Image Recognition
#=============================================================================


if file is None:
    st.text("Please upload an image file")
else:
    with col1:
        model_id= model_id_find(model_selection_button)
        # trick to not use if loop while selecting model file as per model id, comment when using mod_select function
        #name = 'model'
        #exec("%s = %s" % (name, name + '_' + str(model_id)))

        # model loading using mod_select function, uncomment when model size too high
        model = mod_select(model_id)

        img = io.imread(file)
        st.image(img, width=300)
        im_gray = color.rgb2gray(img) # converting to grayscale

        # # change dimension as per train model, uncomment when every model on same dimensions
        dim_w = model.layers[0].output_shape[1]
        dim_h = model.layers[0].output_shape[2]
        img = cv2.resize(im_gray, (dim_w, dim_h))
        img = np.array(img).reshape(-1, dim_w, dim_h, 1)

        

        prediction = model.predict(img)
        # next line will delete model to save ram
        del model
    
    with col2: 
        st.write("Image detected:")
        max = np.max(prediction)
        #st.write(prediction)

        # test and debugging
        category_id= category_pos_fetch(prediction,max)

        # umcomment below 2 lines when loading updated datasource file, with correct id and position
        try:
            category_name = ds.loc[((ds.major_category_id == model_id) & (ds.sub_category_id == category_id)), 'Category'].values[0]
        except:
            category_name="Error 404"
        try:
            category_link = ds.loc[((ds.major_category_id == model_id) & (ds.sub_category_id == category_id)), 'link'].values[0]
        except:
            category_link="https://www.canadiantire.ca/en/hot-deals.html"
        st.markdown(str("__"+category_name+"__"))
        st.write(round(max * 100,2),"%"," Match")
              
        
        ctlink = '[Open on Canadian Tire website]({})'.format(category_link)
        #st.button(ctlink)# cant find documentation for button actions# still in development
        st.markdown(ctlink, unsafe_allow_html=True)

st.image("footer.png")
#=============================================================================
