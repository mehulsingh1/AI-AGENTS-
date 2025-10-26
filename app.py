import streamlit as st
from main import explain_image

st.set_page_config(page_title="Groq Image Explainer", page_icon="🧠", layout="centered")

st.title("🧩 AI Image Recognition Explainer")
st.write("Upload an image and get an intelligent explanation powered by Groq Vision LLM!")

uploaded_img = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_img is not None:
    st.image(uploaded_img, caption="Uploaded Image", use_container_width=True)
    if st.button("Generate Explanation"):
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_img.read())
        with st.spinner("Analyzing with Mehul's AI..."):
            result = explain_image("temp_image.jpg")
        st.success("Explanation Generated:")
        st.write(result)
