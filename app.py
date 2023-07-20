import streamlit as st
from utils import get_modelpaths
from Scripts.video_processor import webcam_input



def main():
    model_list = ["AnimeGANv2_Hayao","AnimeGANv2_Shinka","AnimeGANv2_Paprika"]
    st.title("Real-time Anime to Anime Converter")
    model_name = st.selectbox("Select model name", model_list)
    model_path = get_modelpaths(model_name)

    webcam_input(model_path)



if __name__ == "__main__":
    main()