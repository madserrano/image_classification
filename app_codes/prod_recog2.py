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
import pandas as pd


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
    return tf.keras.models.load_model(model_name)


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

# Load the trained model
import tensorflow as tf

# loading all model files for faster access, switch to mod_select function if model size too high and comment below lines
model_0 = tf.keras.models.load_model('PR_model_0.h5')
model_1 = tf.keras.models.load_model('PR_model_1.h5')
model_2 = tf.keras.models.load_model('PR_model_2.h5')
model_3 = tf.keras.models.load_model('PR_model_3.h5')
model_4 = tf.keras.models.load_model('PR_model_4.h5')



st.image("header.png")



## radio button for categories
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
model_selction_button = st.radio("Select category",('Automotive','Tools & Hardware','Home & Pets','Sports & Recreation','Outdoor Living'))
src="https://www.canadiantire.ca/en/hot-deals.html?adlocation=HP_ASPOT_CanadaDaySuperSale_21326"

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
        model_id= model_id_find(model_selction_button)
        # trick to not use if loop while selecting model file as per model id, comment when using mod_select function
        name = 'model'
        exec("%s = %s" % (name, name + '_' + str(model_id)))

        # model loading using mod_select function, uncomment when model size too high
        # model = mod_select(model_id)

        img = io.imread(file)
        st.image(img, width=300)
        im_gray = color.rgb2gray(img) # converting to grayscale
        if model_id==4:
            img = cv2.resize(im_gray, (90, 90))  # converting to IMG_SIZE 90,90
            img = np.array(img).reshape(-1, 90, 90, 1)

        else:
            img = cv2.resize(im_gray, (28, 28)) # converting to IMG_SIZE 90,90
            img = np.array(img).reshape(-1, 28, 28, 1)
        prediction = model.predict(img)
        # next line will delete model to save ram
        # del model
    
    with col2: 
        st.write("Image detected:")
        max = np.max(prediction)
        # st.write(prediction)

        # test and debugging
        category_id= category_pos_fetch(prediction,max)

        # umcomment below 2 lines when loading updated datasource file, with correct id and position
        category_name = ds.loc[((ds.major_category_id == model_id) & (ds.sub_category_id == category_id)), 'Category'].values[0]
        category_link = ds.loc[((ds.major_category_id == model_id) & (ds.sub_category_id == category_id)), 'sub_category_link'].values[0]

        # delete below 2 line when loading correct ddatsource file
        # category_name = ds.loc[((ds.Category == 'TRAILERS & TOWING ACCESSORIES') & (ds.product_name == 'ATV, MOTORCYCLES, SNOWMOBILE PARTS & ACCESSORIES')), 'major_category_name'].values[0]
        # category_link = ds.loc[((ds.Category == 'TRAILERS & TOWING ACCESSORIES') & (ds.product_name == 'ATV, MOTORCYCLES, SNOWMOBILE PARTS & ACCESSORIES')), 'major_category_link'].values[0]

        st.markdown(str("__"+category_name+"__"))
        st.write("Confidence: ", max)
        ctlink = '[=[Open On CT Website]=]({})'.format(category_link)
        # st.button(ctlink)# cant find documentation for button actions# still in development
        st.markdown(ctlink, unsafe_allow_html=True)

        # if prediction[0:,0] == max :
        #     st.markdown("__FLOOR MATS & LINERS__")
        #     st.write("Confidence: ", max)
        #     st.write("Click this [link](https://www.canadiantire.ca/en/search-results.html?q=FLOOR%20MATS%20%26%20LINERS) to view Floor Mats and Liners products")
        # elif prediction[0:,1] == max :
        #     st.markdown("__BRAKE TOOLS__")
        #     st.write("Confidence: ", max)
        #     st.write("Click this [link](https://www.canadiantire.ca/en/automotive/loan-a-tool/ac-brake-tools.html) to view Brake Tools products")
        # elif prediction[0:,2] == max :
        #     st.markdown("__WHEEL__")
        #     st.write("Confidence: ", max)
        #     st.write("Click this [link](https://www.canadiantire.ca/en/automotive/trailers-towing-accessories/trailer-tires-wheels-tubes.html) to view Wheel products")
        # elif prediction[0:,3] == max :
        #     st.markdown("__TIRE__")
        #     st.write("Confidence: ", max)
        #     st.write("Click this [link](https://www.canadiantire.ca/en/automotive/tires-wheels/tires.html) to view Tire products")
        # elif prediction[0:,4] == max:
        #     st.markdown("__MUFFLER__")
        #     st.write("Confidence: ", max)
        #     st.write("Click this [link](https://www.canadiantire.ca/en/automotive/auto-parts/emission-exhaust-systems/mufflers.html) to view Muffler products")
        # elif prediction[0:,5] == max:
        #     st.markdown("__SPORTS BATTERY__")
        #     st.write("Confidence: ", max)
        #     st.write("Click this [link](https://www.canadiantire.ca/en/search-results.html?q=SPORTS%20BATTERY) to view Sports Battery products")
        # else:
        #     st.write("Unable to detect. Please load another image.")

## iframe for candaian tire app
st.components.v1.iframe(src, scrolling=True)


st.image("footer.png")

#=============================================================================
