import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import numpy as np
import cv2

# --- Side­konfiguration -------------------------
st.set_page_config(page_title="Live Pokémon Scanner", page_icon="🎥")
st.title("Live Pokémon Card Scanner")

st.markdown(
    """
    1. Giv browser­adgang til kameraet.  
    2. Hold dit kort foran kameraet – gen­kendelsen kører live på hver frame.  
    """
)

# --- ICE (STUN) til WebRTC -----------------------
RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]}
    ]
})

# --- Stub-funktion til frame-genkendelse --------
def classify_frame(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    # ===== HER SKAL DIN MODEL SENERE PREDICTE =====
    # Omform img til model-input, kør model.predict, osv.
    # For nu tegner vi bare en placeholder tekst:
    h, w, _ = img.shape
    placeholder = "Genkender kort..."
    cv2.putText(
        img, placeholder, (10, h - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA
    )
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# --- Start live WebRTC-stream -------------------
webrtc_streamer(
    key="live-pokemon-scanner",
    rtc_configuration=RTC_CONFIGURATION,
    video_frame_callback=classify_frame,
    media_stream_constraints={"video": True, "audio": False},
)
