import streamlit as st
import av
import numpy as np
from PIL import Image
from streamlit_webrtc import webrtc_streamer,RTCConfiguration
from Scripts.models import AnimeGAN

RTCConfiguration = RTCConfiguration(
    {"iceServers":[{"urls":["stun:stun.l.google.com:19302"]}]}
)

def webcam_input(model_path):
    """ Take video from webcam and streams converted video
        Args:
            model_path : path of the animeGAN model"

        Returns:
            av.VideoFarme
        """
    st.header("Webcam Live Feed")
    WIDTH = st.sidebar.select_slider('QUALITY (May reduce the speed)', list(range(150, 501, 50)))
    width = WIDTH
    convert_to_anime = AnimeGAN(model_path)
    def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")
        orig_h, orig_w = image.shape[0:2]

        input = np.asarray(Image.fromarray(image).resize((width, int(width * orig_h / orig_w))))

        converted_image = convert_to_anime(input)

        result = Image.fromarray((converted_image * 255).astype(np.uint8))
        image = np.asarray(result.resize((orig_w, orig_h)))
        return av.VideoFrame.from_ndarray(image, format="bgr24")

    ctx = webrtc_streamer(
        key="neural-style-transfer",
        video_frame_callback=video_frame_callback,
        rtc_configuration=RTCConfiguration,
        media_stream_constraints={"video": True, "audio": False},
    )