import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2
import numpy as np

# ─── Sidekonfiguration ────────────────────────────────
st.set_page_config(page_title="Live Pokémon Scanner", page_icon="🎥")
st.title("Live Pokémon Card Scanner")

st.markdown(
    """
    1. Giv browseradgang til kameraet.  
    2. Hold dit kort foran kameraet – genkendelsen kører live på hver frame.  
    """
)

# ─── ICE (STUN + TURN) konfiguration ───────────────────
RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [
        # Google’s offentlige STUN-server
        {"urls": ["stun:stun.l.google.com:19302"]},
        # TURN-server fra Open Relay Project (offentlig, gratis)
        {
            "urls": [
                "turn:openrelay.metered.ca:80",
                "turn:openrelay.metered.ca:443?transport=tcp"
            ],
            "username": "openrelayproject",
            "credential": "openrelayproject"
        }
    ]
})

# ─── Stub-funktion til live-genkendelse ───────────────
def classify_frame(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    h, w, _ = img.shape
    # Placeholder-tekst — byt med model.predict senere
    text = "Genkender kort..."
    cv2.putText(
        img,
        text,
        (10, h - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# ─── Start live WebRTC-stream ─────────────────────────
webrtc_streamer(
    key="live-pokemon-scanner",
    rtc_configuration=RTC_CONFIGURATION,
    video_frame_callback=classify_frame,
    media_stream_constraints={"video": True, "audio": False},
)
