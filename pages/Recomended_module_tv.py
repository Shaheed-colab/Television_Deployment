from sklearn.metrics.pairwise import cosine_similarity
import pickle
import streamlit as st
import joblib

# Page Configuration
st.set_page_config(
    page_title='Television Recommendation System',
    page_icon='📺',
    layout='wide'
)

st.title('Television Recommendation System')

# Load Files
df = pickle.load(open('final_data.pkl', 'rb'))
vectors = model = joblib.load('vectors.joblib')

# Recommendation Function
def recommend(name):

    index = df[df['Model'] == name].index[0]

    similarity = cosine_similarity(
        vectors[index:index+1],
        vectors
    ).flatten()

    distances = sorted(
        list(enumerate(similarity)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_model = []
    recommended_price = []
    recommended_image = []

    for i in distances[1:6]:
        recommended_model.append(
            df.iloc[i[0]]['Model']
        )

        recommended_price.append(
            df.iloc[i[0]]['Price_y']
        )

        recommended_image.append(
            df.iloc[i[0]]['url']
        )

    return (
        recommended_model,
        recommended_price,
        recommended_image
    )


# Select Box
model_name = sorted(df['Model'].unique())

selected_box = st.selectbox(
    'Select a Television',
    model_name
)

# Recommendation Button
if st.button('Recommend TVs'):

    recommended_model, recommended_price, recommended_image = recommend(
        selected_box
    )

    cols = st.columns(5)

    for col, img, model, price in zip(
            cols,
            recommended_image,
            recommended_model,
            recommended_price):

        with col:
            st.image(img, width=180)
            st.markdown(f'**{model}**')
            st.write(f"₹{int(price):,}")
