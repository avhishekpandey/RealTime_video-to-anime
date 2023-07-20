import streamlit as st
import cv2
import numpy as np
from Scripts.models import AnimeGAN
from utils import get_modelpaths



def main():
    model_list = ["AnimeGANv2_Hayao","AnimeGANv2_Shinka","AnimeGANv2_Paprika"]
    st.title("Real-time Anime to Anime Converter")
    model_name = st.selectbox("Select model name", model_list)
    model_path = get_modelpaths(model_name)
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        st.error("Error: Unable to access the webcam.")
        return

    convert_to_anime = AnimeGAN(model_path)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            st.warning("Warning: Unable to capture frame from the webcam.")
            continue


        anime_frame = convert_to_anime(frame)

        st.image(np.hstack((frame, anime_frame)), channels="BGR")

        if st.button("Exit"):
            break

    video_capture.release()


if __name__ == "__main__":
    main()