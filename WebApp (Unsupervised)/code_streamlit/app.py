import streamlit as st
from utils import nmf_predict, user_process
import plotly.io as pio
import pandas as pd

st.set_page_config(
    page_title="David's movie recommender",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

opt = st.sidebar.selectbox("Choose between:",("Movie Recommender", "Movielens Dataset Visualizations"))

if opt == "Movie Recommender":

    st.title(opt)

    col1, col2 = st.columns(2, gap='medium')

    with col1:

        st.image(image="../img/m.png")
        st.markdown("""[Image Source](https://www.pngwing.com/en/free-png-zaqnq)""")

    with col2:

        st.subheader("Please enter 3 movie titles and give them a rating:")


        with st.expander("Open/close movie and ratings input fields"):
            mov1 = st.text_input('Movie title 1:')
            rat1 = st.slider('Rating:',0.5,5.0,step=0.5,key=1)

            mov2 = st.text_input('Movie title 2:')
            rat2 = st.slider('Rating:',0.5,5.0,step=0.5,key=2)

            mov3 = st.text_input('Movie title 3:')
            rat3 = st.slider('Rating:',0.5,5.0,step=0.5,key=3)

        user_input_dict = {}

        user_input_dict[mov1] = rat1
        user_input_dict[mov2] = rat2
        user_input_dict[mov3] = rat3

        guesses = st.checkbox('Wanna see what I guessed from your movie title inputs?')
        
        if guesses:
            st.write(pd.DataFrame.from_dict(user_process(user_input_dict), orient='index', columns=['your_rating']))

        st.write("---")

        if st.button("Get recommendations"):
            with st.spinner('Calculating...'):
                recs_df = nmf_predict(user_input_dict)
            st.success("Here is your result:")
            
            recs_df

else:
    st.title(opt)

    with open('../img/plot.json', 'r') as f:
        fig = pio.from_json(f.read())

    st.plotly_chart(fig)