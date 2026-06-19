import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Television Analytical Module',
    page_icon='📺',
    layout='wide')
df = pd.read_csv('feature_selection_data_1.csv')

# df = df.drop(columns=['Unnamed: 0', 'index'])

st.title('Analytical Module')

fig = st.selectbox('Select Brand Name', df['brand'].unique())

if st.button('Plot Graph'):
    st.header('Histogram')
    fig1 = px.histogram(df[df['brand'] == fig], x='inches', y='Price', color='display_type')
    st.plotly_chart(fig1, use_container_width=True)

    st.header('PIE Chart')
    fig2 = px.pie(df[df['brand'] == fig], names='display_type', values='ppi', color='display_type')
    st.plotly_chart(fig2, use_container_width=True)

    st.header('Scatter Plot')
    fig3 = px.scatter(df[df['brand'] == fig], x='Price', y='inches', size='rom', color='display_type',
                      animation_frame='display_type', size_max=50)
    st.plotly_chart(fig3, use_container_width=True)

    st.header('Bar Plot')
    fig4 = px.bar(df[df['brand'] == fig], x='Spec_Score', y='Rating', color='inches', animation_frame='rom')
    st.plotly_chart(fig4, use_container_width=True)

    st.header('Box Plot')
    fig5 = px.box(df[df['brand'] == fig], x='brand_category', y='Spec_Score')
    st.plotly_chart(fig5, use_container_width=True)

