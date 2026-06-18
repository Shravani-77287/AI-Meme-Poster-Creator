import streamlit as st

from caption_generator import generate_caption
from poster_creator import create_poster

st.title(
    "AI Meme & Poster Creator"
)

topic = st.text_input(
    "Enter Topic"
)

template = st.selectbox(
    "Choose Template",
    [
         "meme1.jpg",
        "meme2.jpg",
        "poster1.jpg",
        "poster2.jpg"
    ]
)

if st.button("Generate"):

    caption = generate_caption(
        topic
    )

    create_poster(
        template,
        caption,
        "generated/output.jpg"
    )

    st.image(
        "generated/output.jpg"
    )

    st.write(
        caption
    )