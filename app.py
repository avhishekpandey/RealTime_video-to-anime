import streamlit as st
import streamlit_webrtc as webrtc
import cv2
import numpy as np
from Scripts.models import AnimeGAN
from utils import get_modelpaths



def main():
    model_list = ["AnimeGANv2_Hayao","AnimeGANv2_Shinka","AnimeGANv2_Paprika"]
    st.title("Real-time Anime to Anime Converter")
    model_name = st.selectbox("Select model name", model_list)
    model_path = get_modelpaths(model_name)

    webrtc_stream = webrtc.VideoStream()

    convert_to_anime = AnimeGAN(model_path)

    while True:
        frame = webrtc_stream.recv()

        anime_frame = convert_to_anime(frame)

        st.image(np.hstack((frame, anime_frame)), channels="BGR")

        if st.button("Exit"):
            break

    webrtc_stream.close()


if __name__ == "__main__":
    main()