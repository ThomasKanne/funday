import streamlit as st
import av
import cv2
import numpy as np
from typing import Literal
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode, RTCConfiguration

# ICE config til HTTPS-hosting
RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
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

class PokemonScanner(VideoProcessorBase):
    effect: Literal["noop", "edges", "text"]

    def __init__(self) -> None:
        self.effect = "noop"

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")

        if self.effect == "edges":
            img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

        elif self.effect == "text":
            h, w, _ = img.shape
            cv2.putText(img, "Genkender Pokémon kort...", (10, h - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # ellers "noop"
        return av.VideoFrame.from_ndarray(img, format="bgr24")

st.set_page_config(page_title="Live Pokémon Scanner", page_icon="🃏")
st.title("🎥 Live Pokémon Card Scanner")

effect = st.radio("Effekt", ["noop", "edges", "text"])

ctx = webrtc_streamer(
    key="pokemon-live",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=PokemonScanner,
    async_processing=True,
)

if ctx.video_processor:
    ctx.video_processor.effect = effect
