import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Live Webcam", page_icon="📷")

st.markdown("### Dit live-kamera")

# Konfiguration af ICE-servere (STUN + TURN)
RTC_CONFIGURATION = {
    "iceServers": [
        # Google’s offentlige STUN-server
        {"urls": ["stun:stun.l.google.com:19302"]},
        # Eksempel på TURN-server (udkommenteret - udfyld med dine egne credentials hvis nødvendigt)
        # {
        #     "urls": [
        #         "turn:turn.example.com:3478?transport=udp",
        #         "turn:turn.example.com:3478?transport=tcp"
        #     ],
        #     "username": "DIT_USERNAME",
        #     "credential": "DIT_PASSWORD"
        # }
    ]
}

# Det enkleste: echo-stream med ICE-konfiguration
webrtc_streamer(
    key="webcam",
    rtc_configuration=RTC_CONFIGURATION,
)

st.info(
    "Klik **Start** og giv browseren adgang til kameraet.\n"
    "Virker kun via HTTPS eller localhost."
)
