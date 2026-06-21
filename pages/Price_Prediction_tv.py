import pickle

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Television Price Prediction',
    page_icon='📺',
    layout='wide')
st.title('Television Price Prediction')

with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

with open('df.pkl', 'rb') as f:
    df = pickle.load(f)

brand = st.selectbox('Select brand ', df['brand'])
ultra_hd = int(st.selectbox('Select Ultra hd', df['ultra_hd'].unique()))
full_hd = int(st.selectbox('Select full hd', df['full_hd'].unique()))
rating = float(st.selectbox('Select Rating', sorted(df['Rating'].unique())))
inches = float(st.selectbox('Select Inches', sorted(df['inches'].unique())))
display_type = st.selectbox('Select Display Type ', df['display_type'])
wifi = int(st.selectbox('Select Wifi', df['wifi'].unique()))
rom = float(st.selectbox('Select ROM', sorted(df['rom'].unique())))
value_score = float(st.selectbox('Select Value Score', sorted(df['value_score'].unique())))
smart_features = float(st.selectbox('Select Smart Features', sorted(df['smart_features'].unique())))
Company_amazon = float(st.selectbox('Select Amazon', sorted(df['Company_amazon'].unique())))
Company_croma = float(st.selectbox('Select Croma', sorted(df['Company_croma'].unique())))
Company_flipkart = float(st.selectbox('Select Flipkart', sorted(df['Company_flipkart'].unique())))
ppi = float(st.selectbox('Select Pixel Per Range', sorted(df['ppi'].unique())))
resolution_width = float(st.selectbox('Select Width', sorted(df['resolution_width'].unique())))
resolution_height = float(st.selectbox('Select Height', sorted(df['resolution_height'].unique())))
fast_charging = float(st.selectbox('Select Fast Charging', sorted(df['fast_charging'].unique())))
ram = float(st.selectbox('Select RAM', sorted(df['ram'].unique())))
Spec_Score = float(st.selectbox('Select Spec Score', sorted(df['Spec_Score'].unique())))
size_category = float(st.selectbox('Select Size Category', sorted(df['size_category'].unique())))
charging_category = float(st.selectbox('Select Charge Category', sorted(df['charging_category'].unique())))
brand_category = st.selectbox('Select Brand Category', df['brand_category'])

if st.button('Press'):
    data = [[brand, ultra_hd, full_hd, rating, inches, display_type,
             wifi, rom, value_score, smart_features, Company_amazon, Company_croma, Company_flipkart, ppi, resolution_width,
             resolution_height, fast_charging, ram, Spec_Score, size_category, charging_category, brand_category]]

    columns = ['brand', 'ultra_hd', 'full_hd', 'Rating', 'inches', 'display_type',
             'wifi', 'rom', 'value_score', 'smart_features', 'Company_amazon', 'Company_croma', 'Company_flipkart', 'ppi', 'resolution_width',
             'resolution_height', 'fast_charging', 'ram', 'Spec_Score', 'size_category', 'charging_category', 'brand_category']
    one_df = pd.DataFrame(data,
                          columns=columns)
    # print(one_df.columns.tolist())
    # st.write(one_df.columns.tolist())

    base_price = np.expm1(pipeline.predict(one_df))[0]

    # st.write(pipeline.feature_names_in_)
    # st.write(pipeline.named_steps['preprocessor'].feature_names_in_)

    # st.write("Pipeline columns:", pipeline.feature_names_in_)
    # st.write("Input columns:", one_df.columns.tolist())

    # st.write(pipeline.feature_names_in_)
    # st.write(one_df.columns.tolist())

    st.metric(
        label='Predicted Television Price',
        value=f'₹{base_price / 10}'
    )